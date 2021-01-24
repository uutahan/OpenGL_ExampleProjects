#CENG487 Assignment2 by
#Umut Utku Tahan
#250201086
#October 2019

from math import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from object_ import Object
from position import Position

class Icosahedron(Object):
    def __init__(self):
        Object.__init__(self,self.get_points())
        
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
        glWindowPos2d(0,3)
        
        for ch in s :
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(ch)))
        
    def increase_subdivisions(self):
        self.divideTriangle()
    def decrease_subdivisions(self):
        self.take_division_back()

    def get_points(self):
        X=.525731112119133606
        Z=.850650808352039932
        N=0
        
        p0=Position(-X,N,Z)
        p1=Position(X,N,Z)
        p2=Position(-X,N,-Z)
        p3=Position(X,N,-Z)
        p4=Position(N,Z,X)
        p5=Position(N,Z,-X)
        p6=Position(N,-Z,X)
        p7=Position(N,-Z,-X)
        p8=Position(Z,X,N)
        p9=Position(-Z,X,N)
        p10=Position(Z,-X,N)
        p11=Position(-Z,-X,N)
        
        points=[p0,p4,p1,p0,p9,p4,p9,p5,p4,p4,p5,p8,p4,p8,p1,p8,p10,p1,p8,p3,p10,p5,p3,p8,p5,p2,p3,
                p2,p7,p3,p7,p10,p3,p7,p6,p10,p7,p11,p6,p11,p0,p6,p0,p1,p6,p6,p1,p10,p9,p0,p11,
                p9,p11,p2,p9,p2,p5,p7,p2,p11]
        
        return points
    
    
    
    
    