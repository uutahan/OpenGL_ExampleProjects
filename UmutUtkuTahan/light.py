#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import *

from position import Position
from box import Box

class Light:
    def __init__(self,ambient,specular,diffuse,position,number):
        
        self.isOn=True
        self.number=number
        self.ambient=ambient
        self.diffuse=diffuse
        self.specular=specular
        self.position=position
        
        self.path=self.get_path(0,50,16)
        
        self.index=0
        
    def switchLight(self):
        if self.isOn==True:
            glDisable(GL_LIGHT0+self.number)
            self.isOn=False
        elif self.isOn==False:
            glEnable(GL_LIGHT0+self.number)
            self.isOn=True
        
    def changePos(self):
        self.index=(self.index+1)%len(self.path)
        
        self.position=[self.path[self.index].x,self.path[self.index].y,self.path[self.index].z,1]
    
    def draw(self,a,b):
        
        glLight( GL_LIGHT0+self.number, GL_DIFFUSE, self.diffuse)
        #glLight( GL_LIGHT1, GL_SPECULAR, self.specular)
        glLight(GL_LIGHT0+self.number, GL_AMBIENT, self.ambient)
        glLight(GL_LIGHT0+self.number,GL_SPOT_CUTOFF,80)
        glLight(GL_LIGHT0+self.number,GL_SPOT_DIRECTION, 	[0.0, -1.0, 0.0,1])
        glLight(GL_LIGHT0+self.number,GL_SPOT_EXPONENT, 2)
   
        glLight(GL_LIGHT0+self.number, GL_POSITION, self.position)
        
        if self.isOn==True:
            glEnable(GL_LIGHT0+self.number)
        
        
        box=Box(1,1,1)
        box.translate(self.position[0],self.position[1],self.position[2])
        
        box.draw(a,b)
    
    def cy_point(self,angle,height,radius):
        return Position(cos(angle)*radius,height,sin(angle)*radius)
    
    def get_path(self,height,sectorCount,radius):
        points=[]
        
        startAngle=0
        endAngle=pi*2
        angleStep=(endAngle-startAngle)/sectorCount 
     
        for i in range(sectorCount): 
            angle=i*angleStep+startAngle
            
            angleNext=(i+1)*angleStep+startAngle
            if (i+1==sectorCount):
                angleNext=endAngle
            
            
            p0=self.cy_point(angle,self.position[1],radius)
            #p1=self.cy_point(angleNext,48,radius)
            #p2=self.cy_point(angleNext,height)
            #p3=self.cy_point(angle,height)
    
            points.append(p0)
            #points.append(p1)
            #points.append(p2)
            #points.append(p3)
        return points