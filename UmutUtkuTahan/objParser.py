#CENG487 Assignment4 by
#Umut Utku Tahan
#250201086
#December 2019

from position import Position
from edge import Edge
from vertex import Vertex
from face import Face

class ObjParser:
    def __init__(self,filename):
        self.filename=filename
        
        self.cornerNumber=self.getCornernNumber()#how much vertices in one face
        
        self.edgeTable=[]        
        self.vertexTable=self.getVertexTable()
        self.faceTable=self.getFaceTable()

    
        
    def getVertexTable(self):
        vertexTable=[]
        vertexPositions=self.get_vertices()
        
        for position in vertexPositions:
            aVertex=Vertex(position)
            
            vertexTable.append(aVertex)
        return vertexTable
    def getFaceTable(self):
        faces=[] #starts from 1.
        f=open(self.filename, "r")
        contents=f.read()
        lines=contents.split('\n')
        
        for line in lines:
            
            if line!="":
                if line[0]=="f":
                    print(line)
                    
                    lineRow=self.get_face_from_line2(line)
                    vertexList=[]
                    for vertexNo in lineRow:
                        vertexList.append(self.vertexTable[vertexNo])
                        
                    aFace=Face(vertexList)  
                    
                    for vertex in vertexList:
                        vertex.addFace(aFace)
                    
                    v1=vertexList[0]
                    v2=vertexList[1]
                    v3=vertexList[2]
                    v4=vertexList[3]
                    
                    edge1=Edge(v1,v2)
                    edge2=Edge(v2,v3)
                    edge3=Edge(v3,v4)
                    edge4=Edge(v1,v4)
                    
                    v1.addEdge(edge1,edge4)
                    v2.addEdge(edge1,edge2)
                    v3.addEdge(edge2,edge3)
                    v4.addEdge(edge3,edge4)
                    
                    self.edgeTable.append(edge1)
                    self.edgeTable.append(edge2)
                    self.edgeTable.append(edge3)
                    self.edgeTable.append(edge4)
                    
                    
            
                    faces.append(aFace)
                        
        return faces
        
    
#    def getVertexTable(self):
#        vertexTable=[]
#        vertexPositions=self.get_vertices()
#        
#        for i in range(len(vertexPositions)):
#            position=vertexPositions[i]
#            adjFacesOfVertex=self.getAdjFacesForVertex(i)
#            adjEdgesOfVertex=self.getAdjEdgesForVertex(i)
#            aVertex=Vertex(position,adjFacesOfVertex,adjEdgesOfVertex)
#            
#            vertexTable.append(aVertex)
#        return vertexTable

    def getVertexTableGivenPositions(self,positions,face_table,edge_table):
        vertexTable=[]
        vertexPositions=positions
        
        for i in range(len(vertexPositions)):
            position=vertexPositions[i]
            adjFacesOfVertex=self.getAdjFacesForVertexGivenFaceTable(i,face_table)
            adjEdgesOfVertex=self.getAdjEdgesForVertexGivenEdgeTable(i,edge_table)
            aVertex=Vertex(position,adjFacesOfVertex,adjEdgesOfVertex)
            
            vertexTable.append(aVertex)
        return vertexTable

    def getAdjFacesForVertexGivenFaceTable(self,vertexIndex,face_table):
        adjFaces=[]
        faceTable=face_table
        for faceIndex in range(len(faceTable)):
            if vertexIndex in faceTable[faceIndex]:
                adjFaces.append(faceIndex)
        return adjFaces
    
    def getAdjEdgesForVertexGivenEdgeTable(self,vertexIndex,edge_table):
        adjEdges=[]
        edgeTable=edge_table
        for edgeIndex in range(len(edgeTable)):
            if edgeTable[edgeIndex].hasVertex(vertexIndex):
                adjEdges.append(edgeIndex)
        return adjEdges

    def getAdjFacesForVertex(self,vertexIndex):
        adjFaces=[]
        faceTable=self.faceTable
        for faceIndex in range(len(faceTable)):
            if vertexIndex in faceTable[faceIndex]:
                adjFaces.append(faceIndex)
        return adjFaces
    def getAdjEdgesForVertex(self,vertexIndex):
        adjEdges=[]
        edgeTable=self.edgeTable
        for edgeIndex in range(len(edgeTable)):
            if edgeTable[edgeIndex].hasVertex(vertexIndex):
                adjEdges.append(edgeIndex)
        return adjEdges
    
#    def getFaceTable(self):
#        faces=[] #starts from 1.
#        f=open(self.filename, "r")
#        contents=f.read()
#        lines=contents.split('\n')
#        
#        for line in lines:
#            
#            if line!="":
#                if line[0]=="f":
#                    faces.append(self.get_face_from_line2(line))
#        return faces
    def get_face_from_line2(self,line):
        
        line=line.strip()
        elems=line.split(" ")
        cornerNumber=len(elems)-1 #how much vertices in one face
        
        lst=[]
        for i in range(cornerNumber):
            lst.append(int(elems[i+1])-1)
        return lst
    def getCornernNumber(self):
        f=open(self.filename, "r")
        contents=f.read()
        lines=contents.split('\n')
        
        line=""
        
        for i in lines:
            
            if i!="":
                if i[0]=="f":
                    line=i
                    break
                
        line=line.strip()
        elems=line.split(" ")
        cornerNumber=len(elems)-1 #how much vertices in one face
        return cornerNumber
    def getEdgeTable(self,face_table):
         faces=face_table
         
         edges=[]
         
         if self.cornerNumber==4:
         
             for i in range(len(faces)):
                
                 edge1=Edge(faces[i][0],faces[i][1])
                 edge2=Edge(faces[i][1],faces[i][2])
                 edge3=Edge(faces[i][2],faces[i][3])
                 edge4=Edge(faces[i][0],faces[i][3])
        
                 if self.checkIfSameEdge(edges,edge1)==False:
                     edge1.addFace(i)
                     edges.append(edge1)
                     
                 else:
                     self.findSameEdge(edges,edge1).addFace(i)
                     
                 if self.checkIfSameEdge(edges,edge2)==False: 
                     edge2.addFace(i)
                     edges.append(edge2)
                 else:
                     self.findSameEdge(edges,edge2).addFace(i)
                     
                 if self.checkIfSameEdge(edges,edge3)==False:   
                     edge3.addFace(i)
                     edges.append(edge3)
                 else:
                     self.findSameEdge(edges,edge3).addFace(i)
                     
                 if self.checkIfSameEdge(edges,edge4)==False:   
                     edge4.addFace(i)
                     edges.append(edge4)
                 else:
                     self.findSameEdge(edges,edge4).addFace(i)
             
             return edges
         
         elif self.cornerNumber==3:
            for i in range(len(faces)):
                
                 edge1=Edge(faces[i][0],faces[i][1])
                 edge2=Edge(faces[i][1],faces[i][2])
                 edge3=Edge(faces[i][0],faces[i][2])
        
                 if self.checkIfSameEdge(edges,edge1)==False:
                     edge1.addFace(i)
                     edges.append(edge1)
                     
                 else:
                     self.findSameEdge(edges,edge1).addFace(i)
                     
                 if self.checkIfSameEdge(edges,edge2)==False: 
                     edge2.addFace(i)
                     edges.append(edge2)
                 else:
                     self.findSameEdge(edges,edge2).addFace(i)
                     
                 if self.checkIfSameEdge(edges,edge3)==False:   
                     edge3.addFace(i)
                     edges.append(edge3)
                 else:
                     self.findSameEdge(edges,edge3).addFace(i)

            return edges
         
    def checkIfSameEdge(self,edges,currEdge):
        flag=False
        for edge in edges:
            if edge.isEqual(currEdge):
                flag=True
        return flag
    
    def findSameEdge(self,edges,currEdge):
        counter=-1
        for edge in edges:
            counter+=1
            if edge.isEqual(currEdge):
                break
        return edges[counter]
            
    
    def get_points(self):
        points=[]
        
        vertices=self.get_vertices()
        f=open(self.filename, "r")
        contents=f.read()
        lines=contents.split('\n')
        
        for line in lines:
            
            if line!="":
                if line[0]=="f":
                    for point in self.get_face_from_line(line):
                        points.append(vertices[point-1])
                   
        return points
    
    
    def get_faces(self):
        vertices=self.get_vertices()
        faces=[]
        
        f=open(self.filename, "r")
        contents=f.read()
        lines=contents.split('\n')
        
        for line in lines:
            if line!="":
                if line[0]=="f":
                    face=[]
                    for point in self.get_face_from_line(line):
                        face.append(vertices[point-1])
                    faces.append(face)
        return faces
    
    def get_vertices(self):
        vertices=[]
        f=open(self.filename, "r")
        contents=f.read()
        lines=contents.split('\n')
        
        for line in lines:
            
            if line!="":
                if line[0]=="v":
                    vertices.append(self.get_vertex_from_line(line))
        return vertices
    
    def get_vertex_from_line(self,line):
        line=line.strip()
        elems=line.split(" ")
        return Position(float(elems[1]),float(elems[2]),float(elems[3]))
    
    def get_face_from_line(self,line):
        line=line.strip()
        elems=line.split(" ")
        cornerNumber=len(elems)-1 #how much vertices in one face
        
        lst=[]
        for i in range(cornerNumber):
            lst.append(int(elems[i+1]))
        return lst
    


            