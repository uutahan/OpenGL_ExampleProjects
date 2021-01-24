#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

import sys
sys.path.append("graphic_position.py")

from homogeneus import Homogeneus

class Vec3d(Homogeneus):
      
    def __init__(self,x,y,z):
        Homogeneus.__init__(self,x,y,z,0)
        

    
    def mapto_position(self):
        return Position(self.x,self.y,self.z)
        
        
        
        
        
        
        
        
    