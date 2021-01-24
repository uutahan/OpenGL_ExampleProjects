#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from position import Position

class Edge:
    
    
    def __init__(self,v0,v1):
        self.vertices=[v0,v1]
        self.middlePoint=self.getMiddlePointOfEdge()
        #self.adjFaces=adjFaces
        #self.adjEdges=adjEdges
    def addFace(self,faceIndex):
        if len(self.adjFaces)<2:          
            self.adjFaces.append(faceIndex)
    
#    def isEqual(self,edge):
#        in1=edge.vertices[0] in self.vertices
#        in2=edge.vertices[1] in self.vertices
#        
#        if in1 and in2:
#            return True
#        else:
#            return False
    def getMiddlePointOfEdge(self): #not edge point
        listOfPos=[]
        for vertex in self.vertices:
            listOfPos.append(vertex.position)
        return self.getAvg(listOfPos)
    
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
    
    def getEdgePoint(self):
        
        posListOfVertices=[self.vertices[0].position,self.vertices[1].position]
        avgVertices=self.getAvg(posListOfVertices)
        
        #---------------------
        
        v1=self.vertices[0]
        v2=self.vertices[1]
        
        v1_faces=v1.adjFaces
        v2_faces=v2.adjFaces
        
        adjFacesOfEdge=[]
        for faceObj in v1_faces:
            
            for face in v2_faces:
                if faceObj.isEqual(face):
                    adjFacesOfEdge.append(faceObj)
        
        if len(adjFacesOfEdge) !=2:
            print("adjFacesOfEdge malfunctioning!!!")
        
        facePoint1=adjFacesOfEdge[0].facePoint
        facePoint2=adjFacesOfEdge[1].facePoint
        
        listOfFacePoints=[facePoint1,facePoint2]
        avgFacePoints=self.getAvg(listOfFacePoints)
        
        edgePoint=self.getAvg([avgFacePoints,avgVertices])
        return edgePoint
        
        
    
    def isEqual(self,edgeObject):
        in1=self.vertices[0].isEqual(edgeObject.vertices[0])
        in2=self.vertices[0].isEqual(edgeObject.vertices[1])
        in3=self.vertices[1].isEqual(edgeObject.vertices[0])
        in4=self.vertices[1].isEqual(edgeObject.vertices[1])
        
        if in1==True and in4==True:
            return True
        if in2==True and in3==True:
            return True
        
        return False
            
    
    
    def toString(self):
        vertex="(V"+str(self.vertices[0])+",V"+str(self.vertices[1])+")"
        
        adjFace="["
        for face in self.adjFaces:
            adjFace+="F"+str(face)+","
        adjFace+="]"
        print(vertex+" " +adjFace)
    
    def hasVertex(self,vertexIndex):
        if vertexIndex in self.vertices:
            return True
        else:
            return False
    
    def getVertices(self):
        return self.vertices