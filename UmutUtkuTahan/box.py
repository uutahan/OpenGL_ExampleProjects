#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019

from math import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from object_ import Object
from position import Position


class Box(Object): 
    def __init__(self,height_x,height_y,height_z):
        Object.__init__(self,self.get_points(height_x,height_y,height_z))
        
        self.height_x=height_x
        self.height_y=height_y
        self.height_z=height_z
    
    def configure(self,height_x,height_y,height_z):
        self.height_x=height_x
        self.height_y=height_y
        self.height_z=height_z
        
        self.points=self.get_points(self.height_x,self.height_y,self.height_z)
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
    
    def draw(self,lineVision,objVision):
        
        if objVision:
            glColor3f(0.5,0.5,0.5)
            glBegin(GL_QUADS)                 
        
            for i in self.points:
                
                glVertex3f(i.x,i.y,i.z)
        
            glEnd()
            
        if lineVision:
            glColor3f(1,0,0)
            glBegin(GL_LINES)                
            for i in self.getFacesFromPoints(4,self.points):
                
                glVertex3f(i[0].x,i[0].y,i[0].z)
                glVertex3f(i[1].x,i[1].y,i[1].z)
                
                glVertex3f(i[1].x,i[1].y,i[1].z)
                glVertex3f(i[2].x,i[2].y,i[2].z)
                
                glVertex3f(i[2].x,i[2].y,i[2].z)
                glVertex3f(i[3].x,i[3].y,i[3].z)
                
                glVertex3f(i[3].x,i[3].y,i[3].z)
                glVertex3f(i[0].x,i[0].y,i[0].z)
        
            glEnd() 
        
#        s = "Subdivision level is "  #print subdivision level on screen
#        s=s+str(self.subdivision_level)
#        glColor3f(0.0, 1.0, 0.0)
#        #glPushMatrix()
#        glWindowPos2d(0,3)
#        
#        for ch in s :
#            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(ch)))
    
    def increase_subdivisions(self):
        self.divideQuad() 
    def decrease_subdivisions(self):
        self.take_division_back()
    
    def getLinePoints(self):
        linePoints=[]
        for i in range(0,len(self.points),6):
            linePoints.append(self.points[i])
            linePoints.append(self.points[i+1])
            linePoints.append(self.points[i+1])
            linePoints.append(self.points[i+2])
            linePoints.append(self.points[i+3])
            linePoints.append(self.points[i+4])
            linePoints.append(self.points[i+4])
            linePoints.append(self.points[i+5])
        return linePoints
    
    def get_points(self,height_x,height_y,height_z):
        points=[]
        
        z=height_z / 2
        x=height_x / 2
        y=height_y / 2
        
        p0=Position( x, y, z ) 
        p1=Position( -x, y, z ) 
        p2=Position( -x, -y, z ) 
        p3=Position( x, -y, z )
        p4=Position( x, y, -z )
        p5=Position( -x, y, -z )
        p6=Position( -x, -y, -z )
        p7=Position( x, -y, -z ) 
        
#        points.append(p0)
#        points.append(p1)
#        points.append(p2)
#        points.append(p3)
        
        points.append(p0)
        points.append(p1)
        points.append(p2)
        points.append(p2)
        points.append(p3)
        points.append(p0)
        
        
#        points.append(p0)
#        points.append(p1)
#        points.append(p5)
#        points.append(p4)
        
        points.append(p0)
        points.append(p1)
        points.append(p5)
        points.append(p5)
        points.append(p4)
        points.append(p0)

        
#        points.append(p0)
#        points.append(p3)
#        points.append(p7)
#        points.append(p4)
        
        points.append(p0)
        points.append(p3)
        points.append(p7)
        points.append(p7)
        points.append(p4)
        points.append(p0)

        
#        points.append(p4)
#        points.append(p5)
#        points.append(p6)
#        points.append(p7)
        
        points.append(p4)
        points.append(p5)
        points.append(p6)
        points.append(p6)
        points.append(p7)
        points.append(p4)

        
#        points.append(p2)
#        points.append(p3)
#        points.append(p7)
#        points.append(p6)
        
        points.append(p2)
        points.append(p3)
        points.append(p7)
        points.append(p7)
        points.append(p6)
        points.append(p2)

        
#        points.append(p1)
#        points.append(p2)
#        points.append(p6)
#        points.append(p5)
        
        points.append(p1)
        points.append(p2)
        points.append(p6)
        points.append(p6)
        points.append(p5)
        points.append(p1)
        
        return points
        
 