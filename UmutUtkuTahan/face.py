#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from position import Position

class Face:
    
    def __init__(self,verticeList): 
        self.vertices=verticeList #consist of vertex objects
        self.facePoint=self.getFacePoint()
    
    def isEqual(self,aFace):
        for i in range(len(self.vertices)):
            if self.vertices[i].isEqual(aFace.vertices[i])==False:
                return False
        
        return True
    
    def isVertexInside(self,vertex):
        for faceVertex in self.vertices:
            if faceVertex.isEqual(vertex):
                return True
        
        return False
    
    def getFacePoint(self):
        listOfPos=[]
        for vertex in self.vertices:
            listOfPos.append(vertex.position)
        return self.getAvg(listOfPos)
    
    def getVertexPositionList(self):
        vertexPosList=[]
        for vertex in self.vertices:
            vertexPosList.append(vertex.position)
        return vertexPosList
    def getAvg(self,listOfPositions):
        totalX=0
        totalY=0
        totalZ=0
        
        counter=0
        for i in listOfPositions:
            counter+=1
            
            totalX+=i.x
            totalY+=i.y
            totalZ+=i.z
        
        x=totalX/counter
        y=totalY/counter
        z=totalZ/counter
        
        return Position(x,y,z)

        