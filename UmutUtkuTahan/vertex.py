#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

class Vertex:
    
    def __init__(self,position):
        self.position=position # coordinates of the vertex (its a position object)
        self.adjFaces=[]
        self.adjEdges=[]
    
    def addFace(self,faceObject):
        if self.checkIfWeHaveFace(faceObject) == False:
            self.adjFaces.append(faceObject)
    
    def checkIfWeHaveFace(self,faceObj):
        for faceObject in self.adjFaces:
            if faceObject.isEqual(faceObj) ==True:
                return True
        
        return False
    
    def checkIfWeHaveEdge(self,edgeObj):
        for edgeObject in self.adjEdges:
            if edgeObject.isEqual(edgeObj) ==True:
                return True
        
        return False
    
    def addEdge(self,edgeObject1,edgeObject2):
        if self.checkIfWeHaveEdge(edgeObject1) == False:
            self.adjEdges.append(edgeObject1)
        if self.checkIfWeHaveEdge(edgeObject2) == False:
            self.adjEdges.append(edgeObject2)
    
    
    
    def toString(self):
        position="("+str(self.position.x)+","+str(self.position.y)+","+str(self.position.z)+")"
        
        faces="["
        for face in self.adjFaces:
            faces+="F"+str(face)+","
        faces+="]"
        
        edges="["
        for edge in self.adjEdges:
            edges+="E"+str(edge)+","
        edges+="]"
        
        return position+" "+faces+" "+edges
    
    def getPosition(self):
        return self.position

    def isEqual(self,vertex):
        cond1=vertex.position.x==self.position.x
        cond2=vertex.position.y==self.position.y
        cond3=vertex.position.z==self.position.z


        if cond1 and cond2 and cond3:
            return True
        else:
            return False

    def setEqualVertexProperties(self,vertex):
        if self.isEqual(vertex):
            vertex.adjEdges=self.adjEdges
            vertex.adjFaces=self.adjFaces




