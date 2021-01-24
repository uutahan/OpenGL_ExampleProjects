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

class Octahedron(Object): #draw using triangles
    def __init__(self,square_height,half_pyramid_height):
        Object.__init__(self,self.get_points(square_height,half_pyramid_height))
        
        self.square_height=square_height
        self.half_pyramid_height=half_pyramid_height
    
    def configure(self,square_height,half_pyramid_height):
        self.square_height=square_height
        self.half_pyraid_height=half_pyramid_height
        
        self.points=self.get_points(self.square_height,self.half_pyramid_height)
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
    
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
    
    def get_points(self,square_height,half_pyramid_height):
        points=[]
        
        sq_c=square_height/sqrt(2)
        py_c=half_pyramid_height/2
        
        p0=Position( sq_c, 0, 0 ) 
        p1=Position( 0, sq_c, 0 )
        p2=Position( 0, 0, py_c )
        p3=Position( -sq_c, 0, 0 ) 
        p4=Position( 0, -sq_c, 0 ) 
        p5=Position( 0, 0, -py_c )
        
        points.append(p2)
        points.append(p0)
        points.append(p1)
        
        points.append(p2)
        points.append(p0)
        points.append(p4)
        
        points.append(p2)
        points.append(p1)
        points.append(p3)
        
        points.append(p2)
        points.append(p4)
        points.append(p3)
        
        points.append(p5)
        points.append(p0)
        points.append(p1)
        
        points.append(p5)
        points.append(p0)
        points.append(p4)
        
        points.append(p5)
        points.append(p1)
        points.append(p3)
        
        points.append(p5)
        points.append(p4)
        points.append(p3)
        
        return points
        
 