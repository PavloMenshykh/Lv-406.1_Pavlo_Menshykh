#importing grasshopper python modules
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.parallel as ghp
import ghpythonlib.components as ghc
import Rhino as rc


#importing generic modules
from math import cos
from math import sin
from math import radians
import random

#Inputs
#anchorp - point3D, anchor point
#depth - integer, recursion cnt
#angle - float, split base angle
#length - float, first branch length
#lvariation - float, length change with each branch
#aran - float, % of randomness in relation to base angle
#lran - float, % of randomness in relation to base length
#radtolen - proportion between starting length branch depth and branch radius

#getting starting point from anchorpoint
x1 = anchorp.X
y1 = anchorp.Y
z1 = anchorp.Z-length #to generate starting vector

#setting base variables
x2 = x1
y2 = y1 
z2 = 0 #to generate starting vector

#base angle
anglerec = 0
anglerech = 0

#list of lines that form the tree, this is the output variable 
treelin = {}
anglest = []

#recursive function
def fractal(depth, x1, y1, z1, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh, branches):
    
    #test if depth>0
    if depth:
        
        #defining random angle variation and length variation
        arn = random.uniform(-angle/100*aran, angle/100*aran)
        lrn = random.uniform(-length/100*lran, length/100*lran)
        
        #defining horizontal rotation angles
        ahor = random.sample(range(0,360), branches)
        
        #removing numbers within tolerance
        ahr = rs.CullDuplicateNumbers(ahor, angleh)
        
        #in a 360 fashion
        if ahr[0]+360-angleh<ahr[-1]:
            del ahr[0]
            
        random.shuffle(ahr)
        
        #previous branch vector
        
        vecst = rg.Point3d(x1, y1, z1)
        vecend = rg.Point3d(x2, y2, z2)
        
        movevec = ghc.Vector2Pt(vecst, vecend, True)[0] #returns vector and it's length
        
        #perpendicular vector rotation plane
        
        rotplane3 = ghc.PlaneNormal(vecend, movevec) #creates plane perpendicular to vector
        plns = ghc.DeconstructPlane(rotplane3) #origin, x, y, z
        rotplane = ghc.ConstructPlane(plns[0], plns[3], plns[2]) #constructing new plane switching x and y planes to make perpendicular
        
        #generating perpendicular vector
        vecperp = ghc.Rotate(movevec, radians(90), rotplane)[0]
        
        #generating vector amplitudes
        leny = (length+lrn)*sin(radians(anglerec+arn))
        lenz = (length+lrn)*cos(radians(anglerec+arn))
        ampy = ghc.Amplitude(vecperp, leny)
        ampz = ghc.Amplitude(movevec, lenz)
        
        #changing branch length dependant on branch depth
        length = length*lvariation
        
        #building points
        endpoint1 = ghc.Move(vecend, ampz)[0] #returns moved object and transformation data
        endpoint = ghc.Move(endpoint1, ampy)[0] #returns moved object and transformation data
        
        #rotating point in a cone fashion
        rotpoint = ghc.Rotate3D(endpoint, anglerech, vecend, movevec)[0] #returns rotated geometry and transformation data
        
        #building line between points
        linegeo = rg.Line(vecend, rotpoint)
        
        #setting coords for next branch
        x1 = x2
        y1 = y2
        z1 = z2
        
        #getting xyz from rotated point
        x2 = rg.Point3d(rotpoint)[0]
        y2 = rg.Point3d(rotpoint)[1]
        z2 = rg.Point3d(rotpoint)[2]
        
        #building a dict of lines with depth as key, and corresponding lines as values
        if depth not in treelin.keys():
            treelin[depth] = [linegeo]
        else: 
            treelin[depth].append(linegeo)
        
        #calling function with different angle parameter for branch splitting
        #calling as many branches as spread within tolerance
        for aa in ahr:
            fractal(depth - 1 , x1, y1, z1, x2, y2, z2, length, angle, angle, lvariation, aran, lran, aa, angleh, branches)
        

        
#first recursive function call
fractal(depth, x1, y1, z1, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh, branches)

#sort dict of branch lines
treelinsorted = {}
branch = depth

for key in treelin.keys():
    treelinsorted[branch] = treelin[key]
    branch -= 1

#maybe implement intersect tests between branches
def removeintersections():
    pass
    #events = Rhino.Geometry.Intersect.Intersection.CurveCurve(curveA, curveB, intersection_tolerance, overlap_tolerance)

#output list
pgons = []

#create ngon branch depth dependant
def ngons(args):
    
    nn, length, lvariation, kk, radtolen, mngon, depth = args
    
    stpnt = ghc.EndPoints(nn)[0] #returns list of two points, start and end
    endpnt = ghc.EndPoints(nn)[1]
    vect = ghc.Vector2Pt(stpnt, endpnt, False)[0] #returns list with vector and vector length
    pln = ghc.PlaneNormal(stpnt, vect) #returns a plane perp to a vector
    radius = length*(lvariation**kk)/radtolen
        
    #reduce details with each branch, but not less than 3
    if mngon-kk+1 <= 3:
        splits = 3
    else:
        splits = mngon-kk+1
    
    pgn = ghc.Polygon(pln, radius, splits, 0)[0] #returns a polygon and its perimeter
    
    if kk == depth and splits == 3:
        geo = ghc.ExtrudePoint(pgn, endpnt) #if last branch than make a pyramid
    else:
        geo = ghc.Extrude(pgn, vect) #extrudes the polygon along vector
    
    return ghc.CapHoles(geo) #caps ends on the extruded brep

#iterate over branches and run ngons func
def makegeo(treelinsorted):
    for kk in treelinsorted.keys():
        for nn in treelinsorted[kk]:
            args = [nn, length, lvariation, kk, radtolen, mngon, depth]
            pgons.append(ngons(args))
            
ghp.run(makegeo, [treelinsorted], True)

def joiner(breps):
    return ghc.SolidUnion(breps)

#joined = joiner(pgons)