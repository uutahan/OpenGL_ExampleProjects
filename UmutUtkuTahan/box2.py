#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from math import *
import numpy as np

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from object_ import Object
from position import Position

from shader_loader import ShaderLoader


class Box(Object): 
    def __init__(self,height_x,height_y,height_z):
        Object.__init__(self,self.get_points_quad(height_x,height_y,height_z))
        
        self.height_x=height_x
        self.height_y=height_y
        self.height_z=height_z
        
        self.shader_loader=ShaderLoader()
    
    def configure(self,height_x,height_y,height_z):
        self.height_x=height_x
        self.height_y=height_y
        self.height_z=height_z
        
        self.points=self.get_points(self.height_x,self.height_y,self.height_z)
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
    
    def drawLines(self):
        
        shaderProgram=self.shader_loader.compile_shader("vertex_shader.vs","frag_shader_2.fs")
        
        
        pointList=self.pointsAsNumbersGivenPoints( self.getLinePoints_quad())
       
        
        np_points = np.array(pointList, dtype=np.float32)
        
           
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, np_points.nbytes, np_points, GL_STATIC_DRAW)
     
       
        position = glGetAttribLocation(shaderProgram, 'position')
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(position)
        
        
        glUseProgram(shaderProgram)
        

      
        glDrawArrays(GL_LINES, 0,len(pointList))
       
        
        glUseProgram(0)
        

        
    def drawObj(self):
    
    
        shaderProgram=self.shader_loader.compile_shader("vertex_shader.vs","frag_shader.fs")
    
     
        np_points = np.array(self.pointsAsNumbers(), dtype=np.float32)
        
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, np_points.nbytes, np_points, GL_STATIC_DRAW)
     
       
        position = glGetAttribLocation(shaderProgram, 'position')
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(position)
        
         
        glUseProgram(shaderProgram)

        glDrawArrays(GL_QUADS, 0, len(self.pointsAsNumbers()))
       
        
        glUseProgram(0)
        

    def draw(self,lineVision,objVision):            
        if objVision:
            self.drawObj()
                
        if lineVision:
            self.drawLines()
           
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
    def getLinePoints_quad(self):
        linePoints=[]
        for i in range(0,len(self.points),4):
            linePoints.append(self.points[i])
            linePoints.append(self.points[i+1])
            linePoints.append(self.points[i+1])
            linePoints.append(self.points[i+2])
            linePoints.append(self.points[i+2])
            linePoints.append(self.points[i+3])
            linePoints.append(self.points[i+3])
            linePoints.append(self.points[i+0])
        return linePoints
    
    def get_points_triangle(self,height_x,height_y,height_z):
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
    
    def get_points_quad(self,height_x,height_y,height_z):
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

        
        points.append(p0)
        points.append(p1)
        points.append(p2)
        points.append(p3)
        

        
        points.append(p0)
        points.append(p1)
        points.append(p5)
        points.append(p4)

        
        points.append(p0)
        points.append(p3)
        points.append(p7)
        points.append(p4)


        
        points.append(p4)
        points.append(p5)
        points.append(p6)
        points.append(p7)


        
        points.append(p2)
        points.append(p3)
        points.append(p7)
        points.append(p6)

        points.append(p1)
        points.append(p2)
        points.append(p6)
        points.append(p5)
        

        
        return points
        
 