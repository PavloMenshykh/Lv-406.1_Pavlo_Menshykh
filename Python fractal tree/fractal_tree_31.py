#importing grasshopper python modules
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.parallel as ghp
import ghpythonlib.components as ghc
import Rhino as rc
import Rhino
import Rhino.Commands as rcc


#importing generic modules
from math import cos
from math import sin
from math import radians
import random
from math import degrees

#Inputs
#anchorp - point3D, anchor point
#depth - integer, recursion cnt
#angle - float, split base angle
#length - float, first branch length
#lvariation - float, length change with each branch
#aran - float, % of randomness in relation to base angle
#lran - float, % of randomness in relation to base length
#radtolen - proportion between starting length branch depth and branch radius

#angle = angle*2

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

verticality /= 100
gchance /= 100
mngon -= 1 #first mngon is defined outside recursive func, so it should enter it with -1

depth = depthstart

#output list
pgons = []

#recursive function
def fractal(depth, x1, y1, z1, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh, branches, verticality, gchance, depthstart, radtolen, radchng, mngon, polygon):
    
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
        
        #pgons.append(polygon)
        #pgons.append(linegeo)
        pgons.append(geocapped)
        
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
        
        for aa in ahr:
            if ((random.randint(40, 99)/100)**depth) < gchance or depth == depthstart+1: #or added to prevent blank trees
                fractal(depth - 1 , x1, y1, z1, x2, y2, z2, length, angle, angle, lvariation, aran, lran, aa, angleh, branches, verticality, gchance, depthstart, radtolen, radchng, mngon, polygon)

#first recursive function call
fractal(depth, x1, y1, z1, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh, branches, verticality, gchance, depthstart, radtolen, radchng, mngon, polygonbase)

def joiner(breps):
    return ghc.SolidUnion(breps)

joined = ghp.run(joiner, [pgons], True)