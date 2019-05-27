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

#list of lines that form the tree, this is the output variable 
treelin = []


#recursive function
def fractal(depth , x2, y2, z2, length, anglerec, angle, lvariation, aran, lran):
    
    #test if depth>0
    if depth:
        
        #defining random angle variation and length variation
        arn = random.uniform(-angle/100*aran, angle/100*aran)
        lrn = random.uniform(-length/100*lran, length/100*lran)
        
        #defining points
        x1 = x2
        y1 = y2
        z1 = z2 
        z2 = z1 + (length+lrn)*cos(radians(anglerec))
        y2 = y1 + (length+lrn)*sin(radians(anglerec))
        
        #changing branch length dependant on branch depth
        length = length*lvariation
        
        #building points
        stpoint = [x1, y1, z1]
        endpoint = [x2, y2, z2]
        
        #building line between points
        treelin.append(rs.AddLine(stpoint, endpoint))
        
        #calling function with different angle parameter for branch splitting
        fractal(depth - 1 , x2, y2, z2, length, (anglerec+angle+arn), angle, lvariation, aran, lran)
        fractal(depth - 1 , x2, y2, z2, length, (anglerec-angle+arn), angle, lvariation, aran, lran)
        
#first recursive function call
fractal(depth, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran)