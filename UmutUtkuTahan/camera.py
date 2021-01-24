#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import *

from vec3d import Vec3d
from object_ import Object

class Camera:

    
    def __init__(self,position,front): #position ,front .. are vector
        self.yaw=-90
        self.pitch=0
        #self.roll=0
           
        self.worldUpAccel=0.01
        
        
        self.position=position
        self.front=front.get_unit_vector()
        
        #self.target=Vec3d(0,0,0)
        #self.direction=(self.position.substract(self.target)).get_unit_vector()
        
        worldUp=Vec3d(0,1,0)
        self.right=(worldUp.cross_product(self.front)).get_unit_vector()
        
        self.up=self.front.cross_product(self.right)

        
    def get_view_matrix(self):
        #self.updateYawPitch()
        #self.updateFrontFromYawPitch()
        #self.front=(self.position.substract(Vec3d(0,0,0))).get_unit_vector()
        return [self.position, self.position.add(self.front), self.up]
        

    def move_right(self,velocity):
        self.position = self.position.substract(self.right.multiply(velocity))
    def move_left(self,velocity):
        self.position = self.position.add(self.right.multiply(velocity))
    def move_forward(self,velocity):
        self.position = self.position.add(self.front.multiply(velocity))
    def move_backward(self,velocity):
        self.position = self.position.substract(self.front.multiply(velocity))
        
    def setFrontY(self,new_front):
       
        self.front=new_front
    
        worldUp=Vec3d(self.front.x,self.front.y+self.worldUpAccel,self.front.z)
        self.right=(worldUp.cross_product(self.front)).get_unit_vector()    
        self.up=self.front.cross_product(self.right)
    def setFrontX(self,new_front,Q):
       
        self.front=new_front

        #at the start if we rotate camera according to y , we can switch to other side with below code
        if (((-0.05<self.front.x) and (self.front.x)<0.05) and ((-0.05<self.front.z) and (self.front.z)<0.05)) :
            #inside critical region

            if Q<0: #if we are going upward
                if self.front.y<0: 
                    self.worldUpAccel=abs(self.worldUpAccel)*-1 
                else:                  
                    self.worldUpAccel=abs(self.worldUpAccel)
            else: #if we are going downward
                
                if self.front.y<0:
                    self.worldUpAccel=abs(self.worldUpAccel)
                else:
                   
                    self.worldUpAccel=abs(self.worldUpAccel)*-1
            

            
        #print("front",self.front.x,self.front.y,self.front.z)
            
        worldUp=Vec3d(self.front.x,self.front.y+self.worldUpAccel,self.front.z)
        #print("worldUp",worldUp.x,worldUp.y,worldUp.z)
        self.right=(worldUp.cross_product(self.front)).get_unit_vector()
    
        self.up=self.front.cross_product(self.right)        
         
    def updateYawPitch(self,xoffset,yoffset):
        #if self.mouseClick:
#            xoffset=self.currX-self.pastX
#            yoffset=self.pastY-self.currY
            
            sensivity=0.0066
            xoffset*=-sensivity
            yoffset*=-sensivity
            
            self.yaw   += xoffset
            self.pitch += yoffset
               
            if self.pitch > 89:
              self.pitch =  89
            if self.pitch < -89:
              self.pitch = -89
    def updateFrontFromYawPitch(self):
        x=cos(radians(self.pitch))*cos(radians(self.yaw))
        y=sin(radians(self.pitch))
        z=cos(radians(self.pitch))*sin(radians(self.yaw))
        
        newfront=Vec3d(x,y,z)
        
        self.front=newfront.get_unit_vector()

    
    def rotate_x(self,center_of_rotation_point,Q):
        
        cam=Object([self.position])
        cam.rotate_point_x(Q,center_of_rotation_point)
        self.position=cam.points[0]
        
        direction=center_of_rotation_point.substract(self.position)
        direction=direction.get_unit_vector()
        #self.front=direction
        self.setFrontX(direction,Q)
    def rotate_y(self,center_of_rotation_point,Q):
#        cam=Object([self.front])
#        cam.rotate_y(0.3)
#        front=cam.points[0]
#        self.front=front.get_unit_vector()
        
        cam=Object([self.position])
        cam.rotate_point_y(Q,center_of_rotation_point)
        self.position=cam.points[0]
        
        direction=center_of_rotation_point.substract(self.position)
        direction=direction.get_unit_vector()
        #self.front=direction
        self.setFrontY(direction)
    def get_normal_coordinates(self,width,height,x,y):
        nx = (2 * x - width ) / width
        ny = -(2 * y - height) / height
        
        return [nx,ny]

    