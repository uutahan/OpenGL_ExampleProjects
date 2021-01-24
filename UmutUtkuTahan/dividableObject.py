#CENG487 Assignment4 by
#Umut Utku Tahan
#250201086
#December 2019

from math import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from object_ import Object
from position import Position
from vertex import Vertex
from edge import Edge
from face import Face

from objParser import ObjParser

class DividableObject(Object):
    #this class only have increase division, decrease division and draw methods.
    #other calculations such as getting faces, making divisions are done in Object class
    def __init__(self,filename):
        self.parser=ObjParser(filename)#instantiate parser with the filename
        
        
        Object.__init__(self,self.parser.get_points())
        self.cornerNumber=len(self.parser.get_faces()[0]) #how many vertices in one face (we need this for drawing)
    
        self.vertexTable=self.parser.vertexTable
        self.faceTable=self.parser.faceTable
        self.edgeTable=self.parser.edgeTable

    
    def increase_subdivisions(self):
        if self.cornerNumber==4:
            #self.divideQuad() 
            #self.points=self.get_points_from_faces(self.updateAll())
            self.subdivide()
            #self.points=self.get_points_from_faces(self.catmull())
        elif self.cornerNumber==3:
            self.divideTriangle()
            
    def decrease_subdivisions(self):
        self.take_division_back()
        
        
    def draw(self,lineVision,objVision):
        if self.cornerNumber==4:
        
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
        
        elif self.cornerNumber==3:
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
            
            
        

    
   