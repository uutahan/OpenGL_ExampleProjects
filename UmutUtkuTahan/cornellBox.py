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
from vertex import Vertex
from edge import Edge
from face import Face

from objParser2 import ObjParser2

class CornellBox(Object):
    #this class only have increase division, decrease division and draw methods.
    #other calculations such as getting faces, making divisions are done in Object class
    def __init__(self,points):
        
        
        Object.__init__(self,points)
       
        #self.cornerNumber=len(self.parser.get_faces()[0]) #how many vertices in one face (we need this for drawing)
        self.cornerNumber=3
        self.rgbColor=[]
        
        self.isRgbColorSet=False
        
        
        self.isMaterialSet=False
    
    def setRgbColor(self,arr):
        self.rgbColor=arr
        self.isRgbColorSet=True
    
    def setMaterial(self,materialObj):
        #self.ambient=materialObj.ambient
        self.shininess=materialObj.shininess
        self.specular=materialObj.specular
        self.emission=materialObj.emission
        #self.diffuse=materialObj.diffuse
        
        self.isMaterialSet=True
        
    def draw(self,lineVision,objVision):
            #glNormal3f( 0, 0, 1)
            glColorMaterial ( GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
            glEnable ( GL_COLOR_MATERIAL )
            
            if self.isMaterialSet==True:
                
                
                
                #glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, self.ambient)
                glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, self.specular)
                glMaterial(GL_FRONT_AND_BACK, GL_EMISSION, self.emission)
                glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, self.shininess)
                #glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.diffuse)

            if objVision:
                
                if self.isRgbColorSet==True:
                    glColor3f(self.rgbColor[0],self.rgbColor[1],self.rgbColor[2])
                else:
                
                    glColor3f(0.5,0.5,0.1)
                glBegin(GL_TRIANGLES)                 
            
                for i in range(0,len(self.points),3):
                    v1=self.points[i].substract(self.points[i+1])
                    v2=self.points[i].substract(self.points[i+2])
                    normal=v1.cross_product(v2)
                    #normal=normal.get_unit_vector()
                    
                    glNormal3f(normal.x,normal.y,normal.z)
                    glVertex3f(self.points[i].x,self.points[i].y,self.points[i].z)
                    glNormal3f(normal.x,normal.y,normal.z)
                    glVertex3f(self.points[i+1].x,self.points[i+1].y,self.points[i+1].z)
                    glNormal3f(normal.x,normal.y,normal.z)
                    glVertex3f(self.points[i+2].x,self.points[i+2].y,self.points[i+2].z)
            
                glEnd() 
        
            if lineVision:
                glColor3f(1,0,0)
                glBegin(GL_LINES)                
                for i in self.getFacesFromPoints(3,self.points):
                    #glNormal3f(i[0].x,i[0].y,i[0].z)
                    glVertex3f(i[0].x,i[0].y,i[0].z)
                    
                    #glNormal3f(i[1].x,i[1].y,i[1].z)
                    glVertex3f(i[1].x,i[1].y,i[1].z)
                    
                    #glNormal3f(i[1].x,i[1].y,i[1].z)
                    glVertex3f(i[1].x,i[1].y,i[1].z)
                    
                    #glNormal3f(i[2].x,i[2].y,i[2].z)
                    glVertex3f(i[2].x,i[2].y,i[2].z)
                    
                    #glNormal3f(i[2].x,i[2].y,i[2].z)
                    glVertex3f(i[2].x,i[2].y,i[2].z)
                    
                    #glNormal3f(i[0].x,i[0].y,i[0].z)
                    glVertex3f(i[0].x,i[0].y,i[0].z)
                    
                glEnd()
                
            glDisable ( GL_COLOR_MATERIAL )
    
   