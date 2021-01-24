#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from vec3d import Vec3d
from homogeneus import Homogeneus

#sys.path.append("graphic1.py")
#sys.path.append("homogeneus.py")

class Position( Homogeneus): #This is a vector class which have homogeneus coordinates
    
    def __init__(self,x,y,z):
        Homogeneus.__init__(self,x,y,z,1)
        
    def mapto_vector(self):
        return Vec3d(self.x,self.y,self.z)
    
    def isEqual(self,pos):
        cond1= self.x==pos.x
        cond2=self.y==pos.y
        cond3=self.z==pos.z
        
        if cond1 and cond2 and cond3:
            return True
        else:
            return False



        
        