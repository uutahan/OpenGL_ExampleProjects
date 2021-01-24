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

class Sphere(Object):
    def __init__(self,longs,lats,radius):
        Object.__init__(self,self.get_points(longs,lats,radius))
        
        self.longs=longs
        self.lats=lats
        self.radius=radius
        
    
        
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
    
    def configure(self,longs,lats,radius):
        self.longs=longs
        self.lats=lats
        self.radius=radius
        
        self.points=self.get_points(self.longs,self.lats,self.radius)
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
        
    def increase_subdivisions(self):
        self.configure(self.longs+1,self.lats+1,self.radius)
        self.subdivision_level+=1
    def decrease_subdivisions(self):
        if((self.longs>1) and (self.lats>1)):
            self.configure(self.longs-1,self.lats-1,self.radius)
            self.subdivision_level-=1
        
    def sp_point(self,longAngle,latAngle,radius):
        return Position(cos(longAngle)*sin(latAngle)*radius, cos(latAngle)*radius, sin(longAngle)*sin(latAngle)*radius) 

#    def setOneOfFaces(self,p0,p1,p2):
#        face1=[]
#        
#        face1.append(p0)
#        face1.append(p1)
#        face1.append(p2)
#        
#        self.faces.append(face1)
            
    
    def get_points(self,longCount,latCount,radius):
        points=[]
        self.faces=[]
    
        startLongAngle=0
        startLatAngle=0
        endLongAngle=pi*2
        endLatAngle=pi
        longAngleStep=(endLongAngle-startLongAngle)/longCount 
        latAngleStep=(endLatAngle-startLatAngle)/latCount 
        for i in range(longCount): 
             for j in range(latCount): 
                 longAngle=i*longAngleStep+startLongAngle
                 latAngle=j*latAngleStep+startLatAngle
    
    
                 longAngleNext=(i+1)*longAngleStep+startLongAngle
                 if (i+1==longCount):
                    longAngleNext=endLongAngle
                    
                 latAngleNext=(j+1)*latAngleStep+startLatAngle
                 if (j+1==latCount):
                    latAngleNext=endLatAngle
                 
    
                 p0=self.sp_point(longAngle, latAngle,radius)
                 p1=self.sp_point(longAngle, latAngleNext,radius)
                 p2=self.sp_point(longAngleNext, latAngle,radius)
                 p3=self.sp_point(longAngleNext, latAngleNext,radius)
    
                 points.append(p0)
                 points.append(p2)
                 points.append(p1)
                 
                 points.append(p3)
                 points.append(p1)
                 points.append(p2)
                 
    
        return points