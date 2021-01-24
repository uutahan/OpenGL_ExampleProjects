#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#October 2019

from box import Box

class Rectangle2d(Box):
    
    
    def __init__(self,height_x,height_y):
        Box.__init__(self,height_x,height_y,0)
        

        
    def draw(self,lineVision,objVision):
        Box.draw(self,lineVision,objVision)
    def getTopRight(self):
        return self.points[0]  
    def getTopLeft(self):
        return self.points[len(self.points)-1]#if we subdivide object we might lose track of left top, this is preventing it.