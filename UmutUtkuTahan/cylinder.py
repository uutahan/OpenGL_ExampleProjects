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

class Cylinder(Object):
    def __init__(self,height,sectorCount,radius):
        Object.__init__(self,self.get_points(height,sectorCount,radius))
        
        self.height=height
        self.radius=radius
        self.sectorCount=sectorCount
        
    def configure(self,height,sectorCount,radius):
        self.height=height
        self.radius=radius
        self.sectorCount=sectorCount
        
        self.points=self.get_points(self.height,self.sectorCount,self.radius)
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
    
    def increase_subdivisions(self):
        self.configure(self.height,self.sectorCount+1,self.radius)
        self.subdivision_level+=1
    def decrease_subdivisions(self):
        if(self.sectorCount>1):
            self.configure(self.height,self.sectorCount-1,self.radius)
            self.subdivision_level-=1
    
    def draw(self,lineVision,objVision):
        if objVision:
            glColor3f(0.5,0.5,0.5)
            glBegin(GL_QUADS)
        
            for i in self.points:
                
                glVertex3f(i.x,i.y,i.z)
        
            glEnd()    
        if objVision:   
            glColor3f(0.5,0.5,0.5)
            glBegin(GL_TRIANGLES)  #close the cylinder
                
            for i in self.get_first_circle_triangle_surface():
                
                glVertex3f(i.x,i.y,i.z)
        
            glEnd()        
        if objVision:
            glColor3f(0.5,0.5,0.5)
            glBegin(GL_TRIANGLES)  #close the cylinder
            
            for i in self.get_second_circle_triangle_surface():
                
                glVertex3f(i.x,i.y,i.z)
        
            glEnd()                     
        if lineVision:
            glColor3f(1,0,0)
            glBegin(GL_LINES)  #close the cylinder
            
            for i in self.get_first_circle_line_surface():
                
                glVertex3f(i.x,i.y,i.z)
        
            glEnd()  
        if lineVision:
            glColor3f(1,0,0)
            glBegin(GL_LINES)  #close the cylinder
            
            for i in self.get_second_circle_line_surface():
                
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
        
        s = "Subdivision level is "  #print subdivision level on screen
        s=s+str(self.subdivision_level)
        glColor3f(0.0, 1.0, 0.0)
        #glPushMatrix()
        glWindowPos2d(0,3)
        
        for ch in s :
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(ch)))
        
    
    def get_first_circle_line_surface(self):
        points=[]
        oldpoints=self.get_first_circle()
        mid=self.get_center(oldpoints)
        for i in range(0,len(oldpoints)):
            points.append(oldpoints[i])
            points.append(mid)

        return points
    def get_first_circle_triangle_surface(self):
        points=[]
        oldpoints=self.get_first_circle()
        mid=self.get_center(oldpoints)
        for i in range(0,len(oldpoints),2):
            points.append(oldpoints[i])
            points.append(oldpoints[i+1])
            points.append(mid)

        return points
    def get_second_circle_line_surface(self):
        points=[]
        oldpoints=self.get_second_circle()
        mid=self.get_center(oldpoints)
        for i in range(0,len(oldpoints)):
            points.append(oldpoints[i])
            points.append(mid)

        return points
    def get_second_circle_triangle_surface(self):
        points=[]
        oldpoints=self.get_second_circle()
        mid=self.get_center(oldpoints)
        for i in range(0,len(oldpoints),2):
            points.append(oldpoints[i])
            points.append(oldpoints[i+1])
            points.append(mid)

        return points
        
    def get_first_circle(self):
        points=[]
        for pointNo in range(len(self.points)):
            n=pointNo%4
            if n==2 or n==3:
                points.append(self.points[pointNo])
        return points
    def get_second_circle(self):
        points=[]
        for pointNo in range(len(self.points)):
            n=pointNo%4
            if n==0 or n==1:
                points.append(self.points[pointNo])
        return points
            
            
    def cy_point(self,angle,height):
        return Position(cos(angle),sin(angle),height)

    def get_points(self,height,sectorCount,radius):
        points=[]
        
        startAngle=0
        endAngle=pi*2
        angleStep=(endAngle-startAngle)/sectorCount 
     
        for i in range(sectorCount): 
            angle=i*angleStep+startAngle
            
            angleNext=(i+1)*angleStep+startAngle
            if (i+1==sectorCount):
                angleNext=endAngle
            
            
            p0=self.cy_point(angle,0)
            p1=self.cy_point(angleNext,0)
            p2=self.cy_point(angleNext,height)
            p3=self.cy_point(angle,height)
    
            points.append(p0)
            points.append(p1)
            points.append(p2)
            points.append(p3)
        return points