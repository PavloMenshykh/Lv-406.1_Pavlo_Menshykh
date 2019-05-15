import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

from math import cos
from math import sin
from math import radians
import random


x1 = 0
y1 = 0
z1 = 0
x2 = x1
y2 = y1
z2 = 0

anglerec = 0 
treelin = []

def fractal(depth , x2, y2, z2, length, anglerec, angle, lvariation, aran, lran):

    if depth:
        
        arn = random.uniform(-angle/100*aran, angle/100*aran)
        lrn = random.uniform(-length/100*lran, length/100*lran)
        x1 = x2
        y1 = y2
        z1 = z2
        x2 = x1 + (length+lrn)*cos(radians(anglerec))
        y2 = y1 + (length+lrn)*sin(radians(anglerec))
        length = length*lvariation
        
        stpoint = [x1, y1, z1]
        endpoint = [x2, y2, z2]
        
        treelin.append(rs.AddLine(stpoint, endpoint))
        fractal(depth - 1 , x2, y2, z2, length, (anglerec+angle+arn), angle, lvariation, aran, lran)
        fractal(depth - 1 , x2, y2, z2, length, (anglerec-angle+arn), angle, lvariation, aran, lran)
        
fractal(depth, x2, y2, z2, length, anglerec, angle, lvariation, aran, lran)