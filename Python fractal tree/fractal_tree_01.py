#importing grasshopper python modules
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

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
treelin = []


#recursive function
def fractal(depth , x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh):
    
    #test if depth>0
    if depth:
        
        #defining random angle variation and length variation
        arn = random.uniform(-angle/100*aran, angle/100*aran)
        lrn = random.uniform(-length/100*lran, length/100*lran)
        
        #defining horizontal rotation angles
        ahor = random.sample(range(0,360), 4)
        #removing numbers within tolerance
        ahr = rs.CullDuplicateNumbers(ahor, angleh)
        #adding random circle rot offset
        hrot = random.uniform(-180, 180)
        
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
        stpoint = [x1, y1, z1]
        endpoint = [x2, y2, z2]
        
        #building line between points
        treelin.append(rs.AddLine(stpoint, endpoint))
        
        #calling function with different angle parameter for branch splitting
        #calling as many branches as spread within tolerance
        try:
            t = ahr[0]
            fractal(depth - 1 , x2, y2, z2, length, (anglerec+angle+arn), angle, lvariation, aran, lran, ahr[0]+hrot, angleh)
        except:
            pass
        try:
            t = ahr[1]
            fractal(depth - 1 , x2, y2, z2, length, (anglerec-angle+arn), angle, lvariation, aran, lran, ahr[1]+hrot, angleh)
        except:
            pass
        try:
            t = ahr[2]
            fractal(depth - 1 , x2, y2, z2, length, (anglerec+angle+arn), angle, lvariation, aran, lran, ahr[2]+hrot, angleh)
        except:
            pass
        try:
            t = ahr[3]
            fractal(depth - 1 , x2, y2, z2, length, (anglerec-angle+arn), angle, lvariation, aran, lran, ahr[3]+hrot, angleh)
        except:
            pass
        
#first recursive function call
fractal(depth, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran, anglerech, angleh)