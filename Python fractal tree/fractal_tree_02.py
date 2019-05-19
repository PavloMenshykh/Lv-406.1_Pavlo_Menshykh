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
z1 = anchorp.Z

#setting base variables
x2 = x1
y2 = y1
z2 = z1

#base angle
anglerec = 0
anglerech = 0

#list of lines that form the tree, this is the output variable 
treelin = {}

anglest = []

#recursive function
def fractal(depth, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh):
    
    #test if depth>0
    if depth:
        
        #defining random angle variation and length variation
        arn = random.uniform(-angle/100*aran, angle/100*aran)
        lrn = random.uniform(-length/100*lran, length/100*lran)
        
        #defining horizontal rotation angles
        ahor = random.sample(range(0,360), 4)
        
        #removing numbers within tolerance
        ahr = rs.CullDuplicateNumbers(ahor, angleh)
        
        #in a 360 fashion
        if ahr[0]+360-angleh<ahr[-1]:
            del ahr[0]
        
        #defining points
        x1 = x2
        y1 = y2
        z1 = z2 
        x2 = x1 - (length+lrn)*sin(radians(anglerec))*sin(radians(anglerech))
        y2 = y1 + (length+lrn)*sin(radians(anglerec))*cos(radians(anglerech))
        z2 = z1 + (length+lrn)*cos(radians(anglerec))
        
        #changing branch length dependant on branch depth
        length = length*lvariation
        
        #building points
        stpoint = rg.Point3d(x1, y1, z1)
        endpoint = rg.Point3d(x2, y2, z2)
        
        #building line between points
        linegeo = rg.Line(stpoint, endpoint)
        
        #building a dict of lines with depth as key, and corresponding lines as values
        if depth not in treelin.keys():
            treelin[depth] = [linegeo]
        else: 
            treelin[depth].append(linegeo)
        
        #calling function with different angle parameter for branch splitting
        #calling as many branches as spread within tolerance
        if len(ahr) > 0:
            fractal(depth - 1 , x2, y2, z2, length, (anglerec+angle+arn), angle, lvariation, aran, lran, ahr[0], angleh)
        if len(ahr) > 1:
            fractal(depth - 1 , x2, y2, z2, length, (anglerec-angle+arn), angle, lvariation, aran, lran, ahr[1], angleh)
        if len(ahr) > 2:
            fractal(depth - 1 , x2, y2, z2, length, (anglerec+angle+arn), angle, lvariation, aran, lran, ahr[2], angleh)
        if len(ahr) > 3:
            fractal(depth - 1 , x2, y2, z2, length, (anglerec-angle+arn), angle, lvariation, aran, lran, ahr[3], angleh)
        
#first recursive function call
fractal(depth, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh)

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

#function that create sphere capped pipes on lines
def pipes(args):
    crv, rad = args
    return ghc.Pipe(crv, rad, 1)

#paralle compute execution of pipes function
linep = []

for kk in treelinsorted.keys():
    args = [[treelinsorted[kk], (length*(lvariation**kk))/radtolen]]
    linep.append(ghp.run(pipes, args, True))

#flatten a list of pipes for output
flatlinep = [y for x in linep for y in x]