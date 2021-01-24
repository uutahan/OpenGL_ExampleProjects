#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

import math

class Homogeneus:
    def __init__(self,x,y,z,w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
    
    def isEqual(self,pos):
        cond1= self.x==pos.x
        cond2=self.y==pos.y
        cond3=self.z==pos.z
        
        if cond1 and cond2 and cond3:
            return True
        else:
            return False
    
    def dot_product(self,vec):
        new_x=vec.x *self.x
        new_y=vec.y *self.y
        new_z=vec.z *self.z
        
        return new_x+new_y+new_z
    
    def cross_product(self,vec):
        new_x=self.y*vec.z - self.z*vec.y
        new_y=self.z*vec.x - self.x*vec.z
        new_z=self.x*vec.y - self.y*vec.x
        
        return Homogeneus(new_x,new_y,new_z,self.w)
    
    def add(self,vec):
        new_x=self.x+vec.x
        new_y=self.y+vec.y
        new_z=self.z+vec.z
        new_w=self.w+vec.w
        
        return Homogeneus(new_x,new_y,new_z,new_w)
    
    def substract(self,vec):
        new_x=self.x-vec.x
        new_y=self.y-vec.y
        new_z=self.z-vec.z
        new_w=self.w-vec.w
        
        return Homogeneus(new_x,new_y,new_z,new_w)
    
    def multiply(self,scalar):
        new_x=self.x*scalar
        new_y=self.y*scalar
        new_z=self.z*scalar
        new_w=self.w*scalar
        
        return Homogeneus(new_x,new_y,new_z,new_w)
    
    def get_length(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    
    def angle_between(self,vec):
        return math.degrees(math.acos(self.dot_product(vec) / (self.get_length() * vec.get_length())))
    
    def get_unit_vector(self):
        return self.multiply(1/self.get_length())
    
    def projection(self,vec):
         return vec.get_unit_vector().multiply((self.dot_product(vec) / vec.get_length() ))
    
    def rotateAroundVector(self,k,Q): #rotate around unit vector k.
        a=self.multiply(math.cos(math.radians(Q))) 
        b=(k.cross_product(self)).multiply(math.sin(math.radians(Q))) 
        c=(k.multiply((k.dot_product(self)))).multiply((1-math.cos(math.radians(Q)))) 

        temp=a.add(b)
        return temp.add(c)                     
        
        