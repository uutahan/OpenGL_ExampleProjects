#CENG487 Assignment5 by
#Umut Utku Tahan
#250201086
#December 2019

from position import Position
from edge import Edge
from vertex import Vertex
from face import Face

class ObjParser2:
    def __init__(self,filename):
        self.filename=filename
        
        self.cornerNumber=self.getCornernNumber()#how much vertices in one face
        self.objects=self.getPointsOfObjects()
        

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
            
    
    def get_points(self,lines):
        points=[]
        
        vertices=self.getAllVertices()
        
        for line in lines:
            
            if line!="":
                if line[0]=="f":
                    for point in self.get_face_from_line(line):
                        points.append(vertices[point-1])
                   
        return points
    
    
    def get_faces(self,lines):
        vertices=self.getAllVertices()
        faces=[]
        
        for line in lines:
            if line!="":
                if line[0]=="f":
                    face=[]
                    for point in self.get_face_from_line(line):
                        face.append(vertices[point-1])
                    faces.append(face)
        return faces
    
    def getPointsOfObjects(self):
        objPoints=[]
        objectFaces=self.getObjectFaces()
        
        for lines in objectFaces:
            points=self.get_points(lines[1:])
            objPoints.append(points)
        return objPoints
    
            
    
    def getObjectFaces(self):
        
        f=open(self.filename, "r")
        contents=f.read()
        objects=contents.split('g ')
        
        objectLines=[]
        
        for objectLine in objects:
            line=objectLine.split("\n")
            line=self.remove_values_from_list(line,"")
            
            
            
            if line[0][0]!="#" and line[0]!="default":
                objectLines.append(line)
                
        
        return objectLines
    
    def getAllVertices(self):
        
        f=open(self.filename, "r")
        contents=f.read()
        lines=contents.split('\n')
        
        return self.get_vertices(lines)
        
            
    def remove_values_from_list(self,the_list, val):
        return [value for value in the_list if value != val]
    def get_vertices(self,lines):
        vertices=[]
        
        for line in lines:
            
            if line!="":
                if line[0]=="v":
                    vertices.append(self.get_vertex_from_line(line))
        
#        for i in vertices:
#            print(i.x,i.y,i.z)
#        print("-----------")
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
    


            