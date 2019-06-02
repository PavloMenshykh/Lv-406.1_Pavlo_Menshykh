#importing grasshopper python modules
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.parallel as ghp
import ghpythonlib.components as ghc

#importing generic modules
from math import cos
from math import sin
from math import radians
import random
from math import degrees

#Inputs
#anchorp - point3D, anchor point
#depthstart - integer, recursion cnt
#branches - integer, maximum amount of horizontal branches
#angle - float, split base angle
#angleh - float, minimum horizontal branches spacing
#length - float, first branch length
#lvariation - float, length change with each branch
#aran - float, % of randomness in relation to base angle
#lran - float, % of randomness in relation to base length
#hrandom  - boolean, if horizontal branches evenly spaced or random
#radtolen - float, proportion between starting length branch depth and branch radius
#radchng - float, extra radius changes exept for one derived from lvariation
#mngon - interger, starting polygon vertex count
#verticality - float, angle smaller variation with higher branches, adds realism
#gchance - chance that a branch will stop, increases with depth
#leaflen - float, length of leaves
#leafwidth - float, width of leaves
#maxleaves - int, maximum number of leaves growing from leafpoint
#leavesperbranch - int, maximum number of leaf growth points on last branch

#getting starting point from anchorpoint
x1 = anchorp.X
y1 = anchorp.Y
z1 = anchorp.Z-length #to generate starting vector

#setting base variables
x2 = x1
y2 = y1 
z2 = anchorp.Z #to generate starting vector

#setting first polygon
radiusbase = length/radtolen
stpntbase = rg.Point3d(x1, y1, z1)
stpntbaseend = rg.Point3d(x2, y2, z2)
vecbase = rg.Line(stpntbase, stpntbaseend)
plnbase = ghc.PlaneNormal(stpntbaseend, vecbase) #returns a plane perp to a vector
polygonbase = ghc.Polygon(plnbase, radiusbase, mngon, 0)[0] #returns a polygon and its perimeter

#base angle
anglerec = 0
anglerech = 0
cluster = [1]
branch_cluster = cluster[0]

verticality /= 100
gchance /= 100
mngon -= 1 #first mngon is defined outside recursive func, so it should enter it with -1

depth = depthstart

#output list
pgons = {}
pgnosout = [] #for debug purposes
leaves = []

#recursive function
def fractal(depth, x1, y1, z1, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh, branches, verticality, gchance, depthstart, radtolen, radchng, mngon, polygon, branch_cluster):
    
    #test if depth>0
    if depth:
        
        #defining random angle variation and length variation
        arn = random.uniform(-angle/100*aran, angle/100*aran)
        lrn = random.uniform(-length/100*lran, length/100*lran)
        
        if hrandom == True:
            #defining horizontal rotation angles
            ahor = random.sample(range(0,360), branches)
            
            #removing numbers within tolerance
            ahr = rs.CullDuplicateNumbers(ahor, angleh)
            
            #in a 360 fashion
            if ahr[0]+360-angleh<ahr[-1]:
                del ahr[0]
        else:
            #generating evenly distributed angles
            ahr = range(0, 360+1, 360//branches)[:-1]
        
        #previous branch vector
        vecst = rg.Point3d(x1, y1, z1)
        vecend = rg.Point3d(x2, y2, z2)
        movevec = ghc.Vector2Pt(vecst, vecend, True)[0] #returns vector and it's length
        
        #perpendicular vector 
        rotplane3 = ghc.PlaneNormal(vecend, movevec) #creates plane perpendicular to vector
        plns = ghc.DeconstructPlane(rotplane3) #origin, x, y, z
        rotplane = ghc.ConstructPlane(plns[2], plns[1], plns[3]) #constructing new plane switching x and y planes to make perpendicular
        
        #generating perpendicular vector
        vecperp = ghc.Rotate(movevec, radians(90), rotplane)[0]
        
        #generating vector amplitudes
        leny = (length+lrn)*sin(radians((anglerec+arn)*(1-(verticality**depth))))
        lenz = (length+lrn)*cos(radians(anglerec+arn))
        ampy = ghc.Amplitude(vecperp, leny)
        ampz = ghc.Amplitude(movevec, lenz)
        
        #changing branch length dependant on branch depth
        length = length*lvariation
        
        #building points
        endpoint1 = ghc.Move(vecend, ampz)[0] #returns moved object and transformation data
        endpoint = ghc.Move(endpoint1, ampy)[0] #returns moved object and transformation data
        
        #rotating point in a cone fashion
        rotpoint = ghc.Rotate3D(endpoint, radians(anglerech), vecend, movevec)[0] #returns rotated geometry and transformation data
        
        #building line between points
        linegeo = rg.Line(vecend, rotpoint)
        
        #defining recursion depth
        key = depthstart+1-depth
        
        #building geometry
        pln = ghc.PlaneNormal(rotpoint, linegeo) #returns a plane perp to a vector
        radius = length*(radchng**(key))/radtolen
        
        #reduce details with each branch, but not less than 3
        if mngon-key+1 <= 3:
            splits = 3
        else:
            splits = mngon-key+1
            
        polygonend = ghc.Polygon(pln, radius, splits, 0)[0] #returns a polygon and its perimeter
        
        #aligning curves for loft creation
        crvst = ghc.EndPoints(polygon)[0]
        pntcld = ghc.Discontinuity(polygonend, 1) #returns points and point parameters
        
        #finind seam point
        closest_point = ghc.ClosestPoint(crvst, pntcld[0]) #returns closest point, closest point index, distance between closest points
        seampnt = pntcld[1][closest_point[1]]
        polygonend = ghc.Seam(polygonend, seampnt)
        
        lcurves = [polygon, polygonend]
        
        #building geometry
        if depth == 1 and splits == 3:
            geo = ghc.ExtrudePoint(polygon, rotpoint) #if last branch than make a pyramid
        else:
            geo = rg.Brep.CreateFromLoft(lcurves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        
        #make solid
        geocapped = ghc.CapHoles(geo)
        
        #building a dict of geo with depth as key, and geo as values, for more efficient joins
        
        if branch_cluster not in pgons.keys():
            pgons[branch_cluster] = [geocapped]
        else: 
            pgons[branch_cluster].append(geocapped)
        
        pgnosout.append(geocapped)
        
        #setting coords for next branch
        x1 = x2
        y1 = y2
        z1 = z2
        
        #getting xyz from rotated point
        x2 = rg.Point3d(rotpoint)[0]
        y2 = rg.Point3d(rotpoint)[1]
        z2 = rg.Point3d(rotpoint)[2]
        
        #setting base polygon for next branch
        polygon = polygonend
        
        #calling function with different angle parameter for branch splitting
        #calling as many branches as spread within tolerance
        #filling dict with branch clusters
        cluster.append(cluster[-1]+1)
        branch_cluster=cluster[-1]
        
        if depth != 1:
            for aa in ahr:
                if ((random.randint(40, 99)/100)**depth) < gchance or depth == depthstart+1: #or added to prevent blank trees
                    fractal(depth - 1 , x1, y1, z1, x2, y2, z2, length, angle, angle, lvariation, aran, lran, aa, angleh, branches, verticality, gchance, depthstart, radtolen, radchng, mngon, polygon, branch_cluster)
        else:
            #leaf logic
            if leavesperbranch > 0:
                
                #vector for leaf growth spread
                leafpntvec = ghc.Vector2Pt(vecend, rotpoint, True)[0]
                
                #setting leaf growth position on last barnch
                #leafpnt list
                lastbranchlength = ghc.Length(linegeo)
                leaves_list = [] 
                if leavesperbranch > 1:
                    for lengthparam in random.sample(range(0, int(lastbranchlength)), leavesperbranch-1):
                        leaves_list.append(lengthparam)
                leaves_list.append(lastbranchlength)
                for leafpnt in leaves_list:
                    leafamp = ghc.Amplitude(leafpntvec, leafpnt)
                    leafpoint = ghc.Move(vecend, leafamp)[0]
                    
                    #plane for leaf generation
                    linetocenter = ghc.Line(stpntbase, leafpoint)
                    planetocenter = ghc.PlaneNormal(leafpoint, linetocenter)
                    
                    #create an imaginary circle with leaflen radius and populate it with points for random leaf generation
                    #testcircle = ghc.Circle(leafpoint, leaflen)
                    testcircle = ghc.CircleCNR(leafpoint, linetocenter, leaflen)
                    circlesurf = ghc.BoundarySurfaces(testcircle)
                    leafendpnts = ghc.PopulateGeometry(circlesurf, random.randint(2, maxleaves+1), random.randint(1,500)) #has to be over 1 for correct iteration, else iterates over xyz values
                    
                    #iterate over random number of generated points
                    for pp in leafendpnts:
                        #random z move
                        zmove = rg.Vector3d(0, 0, 1)
                        moveamp = random.uniform(-leaflen/3, leaflen/5)
                        ampzmove = ghc.Amplitude(zmove, moveamp)
                        llendpnt = ghc.Move(pp, ampzmove)[0]
                        
                        #setting a leaf centerline vector
                        leafvector = ghc.Vector2Pt(leafpoint, llendpnt, True)[0]
                        #defining leaf center point as avarage of st and end pnts
                        midpnt = ghc.Average([leafpoint, llendpnt])
                        
                        #generating perpendicular vector
                        vecperpleaf = ghc.Rotate(leafvector, radians(90), planetocenter)[0]
                        leafperpamp = ghc.Amplitude(vecperpleaf, random.uniform((leafwidth/2)/5*4, (leafwidth/2)/5*6))
                        
                        #moving mid point to both sides
                        midpnt1 = ghc.Move(midpnt, leafperpamp)[0]
                        midpnt2 = ghc.Move(midpnt, -leafperpamp)[0]
                        
                        #leaf geo
                        leafgeo = rg.NurbsSurface.CreateFromCorners(leafpoint, midpnt1, llendpnt, midpnt2)
                        
                        leaves.append(leafgeo)
            
#first recursive function call
fractal(depth, x1, y1, z1, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh, branches, verticality, gchance, depthstart, radtolen, radchng, mngon, polygonbase, branch_cluster)

"""
#CAN THROW ERRORS BECAUSE OF BOOLEAN UNION LOGIC 
data_for_parallel = []
data_single = []
for key in pgons.keys():
    if len(pgons[key]) != 1:
        branch_geo = []
        for nn in pgons[key]:
            branch_geo.append(nn)
        data_for_parallel.append(branch_geo)
    else:
        data_single.append(pgons[key][0])


def joiner(breps):
    try:
        union = ghc.SolidUnion(breps)
    except:
        return breps
    else:
        return union 
joined = []

for data in data_for_parallel:
    joined.append(joiner(data))
#joined = ghp.run(joiner, data_for_parallel, True)
#treeoutput = [joined, data_single]


#print(cluster)
#print(pgons)
#print(data_for_parallel)
"""