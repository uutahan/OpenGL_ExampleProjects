#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019

from object_ import Object
from position import Position

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Grid(Object):
    def __init__(self):
        Object.__init__(self,self.get_points())
    def get_points(self):
        points=[]
        
        half_size=10
        for i in range(-half_size,half_size,1):           
            points.append(Position(i,0,-half_size));
            points.append(Position(i,0,half_size));
    
            points.append(Position(-half_size,0,i));
            points.append(Position(half_size,0,i));
        
        return points
    
    def draw(self,lineVision,objVision):
        glDisable(GL_DEPTH_TEST) #disable depth test for drawing x and y axis in different color
        
        glBegin(GL_LINES)                
    
        for i in self.points:
            glColor3f(1,1,1)
            glVertex3f(i.x,i.y,i.z)
    
        glEnd() 
        
        glBegin(GL_LINES)  
              
        glColor3f(0,1,0)
        glVertex3f(-10,0,0)
        glVertex3f(10,0,0)
        
        glColor3f(0,0,1)
        glVertex3f(0,0,10)
        glVertex3f(0,0,-10)
  
        glEnd()
        
        glPointSize(5)
        glBegin(GL_POINTS)
        glColor3f(1,0,0)
        glVertex3f(0,0,0)
        glEnd()
        
        
        
        glEnable(GL_DEPTH_TEST) #enable depth test back
        