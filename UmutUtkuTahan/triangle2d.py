#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#October 2019

from object_ import Object
from position import Position

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import *

class Triangle2d(Object):
    def __init__(self,length):
        Object.__init__(self,self.get_points(length))
    def increase_subdivisions(self):
        self.divideTriangle()
    def decrease_subdivisions(self):
        self.take_division_back()
    def draw(self,lineVision,objVision):
        if objVision:
            glColor3f(0.5,0.5,0.5)
            glBegin(GL_TRIANGLES)                 
        
            for i in self.points:
                
                glVertex3f(i.x,i.y,i.z)
        
            glEnd() 
        
        if lineVision:
            glColor3f(1,0,0)
            glBegin(GL_LINES)                
            for i in self.getFacesFromPoints(3,self.points):
                
                glVertex3f(i[0].x,i[0].y,i[0].z)
                glVertex3f(i[1].x,i[1].y,i[1].z)
                
                glVertex3f(i[1].x,i[1].y,i[1].z)
                glVertex3f(i[2].x,i[2].y,i[2].z)
                
                glVertex3f(i[2].x,i[2].y,i[2].z)
                glVertex3f(i[0].x,i[0].y,i[0].z)
                
            glEnd()
        
        s = "Subdivision level is "  #print subdivision level on screen
        s=s+str(self.subdivision_level)
        glColor3f(0.0, 1.0, 0.0)
        #glPushMatrix()
        glWindowPos2d(453,3)
        
        for ch in s :
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(ch)))
    def get_points(self,length): #length of an edge of triangle (all edges have same length)
        points=[]
        if length>0:
            p1=Position(-length/2,0,0)
            p2=Position(length/2,0,0)
            
            b=(sqrt(3)*length)/2
            
            p3=Position(0,b,0)
            
            points.append(p1)
            points.append(p2)
            points.append(p3)
        
        return points
    def getBottomRight(self):
        return self.points[len(self.points)-2]#if we subdivide object we might lose track of left top, this is preventing it.
    def getBottomLeft(self):
        return self.points[0]

            
        