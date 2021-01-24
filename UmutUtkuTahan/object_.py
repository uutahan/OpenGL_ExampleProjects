#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

from mat3d import Mat3d
from homogeneus import Homogeneus
from position import Position

from edge import Edge
from vertex import Vertex
from face import Face
from mesh import Mesh

class Transformations(object): #for keeping track of transformations
    Rotate_X=1
    Rotate_Y=2
    Rotate_Z=3
    Translate=4
    Scale=5

class Object: #whenever set your points dont forget to set your matrix and center!
    
    transformations=[] #keeps track of transformations with help of the enum.
    
    
    def __init__(self,points): #points are vec3d(can be in homogeneus coordinates) objects in a list
        self.points=points
            
        self.matrix=self.get_matrix(points)

        self.center=self.get_center(points)
        
        mat=Mat3d([])
        self.transformation_matrix=mat.get_scale_matrix(1)
        
        self.subdivision_level=0
        self.subdivisionMemory=[] #for going back and forth in subdivision level (caching the data)
        self.subdivisionMemory.append(points)
        
        self.meshMemory=[]
        #note that we are not forgeting the structure of original object, it stays in our array(the cache)
        self.vertexTable=[]
        self.faceTable=[]
        self.edgeTable=[]
    
    def pointsAsNumbers(self):
        arr=[]
        for vec in self.points:
            arr.append(vec.x)
            arr.append(vec.y)
            arr.append(vec.z)
        return arr
    def pointsAsNumbersGivenPoints(self,points):
        arr=[]
        for vec in points:
            arr.append(vec.x)
            arr.append(vec.y)
            arr.append(vec.z)
        return arr
    
    
    def get_matrix(self,points):
        m=[]
        for i in points:
            k=[i.x,i.y,i.z,i.w]
            
            
            m.append(k)
        return Mat3d(m).transpose()
    
    
    def set_points(self,new_matrix):
        new_matrix=new_matrix.transpose()
        points=[]
        for i in new_matrix.lst:
            a_point=[]
            for j in i:
                a_point.append(j)
            p1=Homogeneus(a_point[0],a_point[1],a_point[2],a_point[3])
            
            points.append(p1)
        
        self.points=points
        self.matrix=self.get_matrix(points)
        self.center=self.get_center(points)
        
   
        
    def get_center(self,points):
        total_x=0
        total_y=0
        total_z=0

        counter=0

        for i in points:
            total_x+=i.x
            total_y+=i.y
            total_z+=i.z

            counter+=1

        x=total_x/counter
        y=total_y/counter
        z=total_z/counter

        return Position(x,y,z)

	
    def apply_transformation_matrix(self):
        m=Mat3d([])
        new_matrix=self.transformation_matrix.matrixMul(self.matrix)
        
        self.set_points(new_matrix)

        
	
    def rotate_x(self,Q):
        m=Mat3d([])
        new_matrix=m.get_rotation_matrix_x_axis(Q).matrixMul(self.matrix)
        
        self.set_points(new_matrix)
    
        self.transformations.append(Transformations.Rotate_X)
        self.transformation_matrix=m.get_rotation_matrix_x_axis(Q).matrixMul(self.transformation_matrix)
        
    def rotate_z(self,Q):
        m=Mat3d([])
        new_matrix=m.get_rotation_matrix_z_axis(Q).matrixMul(self.matrix)
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Rotate_Z)
        self.transformation_matrix=m.get_rotation_matrix_z_axis(Q).matrixMul(self.transformation_matrix)
        
    def rotate_y(self,Q):
        m=Mat3d([])
        new_matrix=m.get_rotation_matrix_y_axis(Q).matrixMul(self.matrix)
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Rotate_Y)
        self.transformation_matrix=m.get_rotation_matrix_y_axis(Q).matrixMul(self.transformation_matrix)
        
    def translate(self,x,y,z):
        m=Mat3d([])
        new_matrix=m.get_translation_matrix(x,y,z).matrixMul(self.matrix)
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Translate)
        self.transformation_matrix=m.get_translation_matrix(x,y,z).matrixMul(self.transformation_matrix)
    
    def rotate_point_z(self,Q,point): #rotates according to a point, and according to z axis.
        m=Mat3d([])
        new_matrix=m.get_translation_matrix(-point.x,-point.y,-point.z).matrixMul(self.matrix)
        new_matrix=m.get_rotation_matrix_z_axis(Q).matrixMul(new_matrix)
        new_matrix=m.get_translation_matrix(point.x,point.y,point.z).matrixMul(new_matrix)
        
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Translate)
        self.transformations.append(Transformations.Rotate_Z)
        self.transformations.append(Transformations.Translate)
        
        self.transformation_matrix=m.get_translation_matrix(-point.x,-point.y,-point.z).matrixMul(self.transformation_matrix)
        self.transformation_matrix=m.get_rotation_matrix_z_axis(Q).matrixMul(self.transformation_matrix)
        self.transformation_matrix=m.get_translation_matrix(point.x,point.y,point.z).matrixMul(self.transformation_matrix)

    def rotate_point_x(self,Q,point): #rotates according to a point, and according to z axis.
        m=Mat3d([])
        new_matrix=m.get_translation_matrix(-point.x,-point.y,-point.z).matrixMul(self.matrix)
        new_matrix=m.get_rotation_matrix_x_axis(Q).matrixMul(new_matrix)
        new_matrix=m.get_translation_matrix(point.x,point.y,point.z).matrixMul(new_matrix)
        
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Translate)
        self.transformations.append(Transformations.Rotate_Z)
        self.transformations.append(Transformations.Translate)
        
        self.transformation_matrix=m.get_translation_matrix(-point.x,-point.y,-point.z).matrixMul(self.transformation_matrix)
        self.transformation_matrix=m.get_rotation_matrix_x_axis(Q).matrixMul(self.transformation_matrix)
        self.transformation_matrix=m.get_translation_matrix(point.x,point.y,point.z).matrixMul(self.transformation_matrix)

    def rotate_point_y(self,Q,point): #rotates according to a point, and according to z axis.
        m=Mat3d([])
        new_matrix=m.get_translation_matrix(-point.x,-point.y,-point.z).matrixMul(self.matrix)
        new_matrix=m.get_rotation_matrix_y_axis(Q).matrixMul(new_matrix)
        new_matrix=m.get_translation_matrix(point.x,point.y,point.z).matrixMul(new_matrix)
        
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Translate)
        self.transformations.append(Transformations.Rotate_Z)
        self.transformations.append(Transformations.Translate)
        
        self.transformation_matrix=m.get_translation_matrix(-point.x,-point.y,-point.z).matrixMul(self.transformation_matrix)
        self.transformation_matrix=m.get_rotation_matrix_y_axis(Q).matrixMul(self.transformation_matrix)
        self.transformation_matrix=m.get_translation_matrix(point.x,point.y,point.z).matrixMul(self.transformation_matrix)
    
    def scale(self,scalar):
        m=Mat3d([])
        new_matrix=m.get_scale_matrix(scalar).matrixMul(self.matrix)
        
        self.set_points(new_matrix)
        
        self.transformations.append(Transformations.Scale)
        
        self.transformation_matrix=m.get_scale_matrix(scalar).matrixMul(self.transformation_matrix)
        
    def getFacesFromPoints(self,cornerNumber,points): #for triangle cornerNumber is 3, for square its 4...
        faces=[]
        for i in range(0,len(points),cornerNumber):
            face=[]
            for j in range(cornerNumber):
                face.append(points[i+j])
            faces.append(face)  
        return faces
    
    def divideQuadSurface(self):
        #when making divisions make it according to start position always, and then account for accumulated transformations
        faces=self.getFacesFromPoints(4,self.subdivisionMemory[self.subdivision_level]) 
        new_faces=[]
            
        for face in faces:
            
            middle_point=self.get_center(face)
         
            edge1=[face[0],face[1]]
            edge2=[face[1],face[2]]
            edge3=[face[2],face[3]]
            edge4=[face[3],face[0]]
            
            edge_mid1=self.get_center(edge1)
            edge_mid2=self.get_center(edge2)
            edge_mid3=self.get_center(edge3)
            edge_mid4=self.get_center(edge4)
            
            new_face1=[face[0],edge_mid1,middle_point,edge_mid4]
            new_face2=[edge_mid1,face[1],edge_mid2,middle_point]
            new_face3=[middle_point,edge_mid2,face[2],edge_mid3]
            new_face4=[edge_mid4,middle_point,edge_mid3,face[3]]

            new_faces.append(new_face1)
            new_faces.append(new_face2)
            new_faces.append(new_face3)
            new_faces.append(new_face4)
        
        points=self.get_points_from_faces(new_faces)
        self.subdivisionMemory.append(points)
        return points
    
    def divideTriangleSurface(self):
        faces=self.getFacesFromPoints(3,self.subdivisionMemory[self.subdivision_level]) 
        new_faces=[]
        
        for face in faces:
            edge1=[face[0],face[1]]
            edge2=[face[1],face[2]]
            edge3=[face[2],face[0]]
            
            edge_mid1=self.get_center(edge1)
            edge_mid2=self.get_center(edge2)
            edge_mid3=self.get_center(edge3)
            
            new_face1=[face[0],edge_mid1,edge_mid3]
            new_face2=[edge_mid1,edge_mid2,edge_mid3]
            new_face3=[edge_mid3,edge_mid2,face[2]]
            new_face4=[edge_mid1,face[1],edge_mid2]
            
            new_faces.append(new_face1)
            new_faces.append(new_face2)
            new_faces.append(new_face3)
            new_faces.append(new_face4)
        
        points=self.get_points_from_faces(new_faces)
        self.subdivisionMemory.append(points)
        return points

    def get_points_from_faces(self,faces):
        points=[]
        for face in faces:
            for point in face:
                points.append(point)
        
        return points
    
    def take_division_back(self):
        length=len(self.subdivisionMemory)
        if (length>1) and (self.subdivision_level>0):
            self.points=self.subdivisionMemory[self.subdivision_level-1]
            self.matrix=self.get_matrix(self.points)
            self.center=self.get_center(self.points)
            self.apply_transformation_matrix()
        
            self.subdivision_level-=1;
    
    def divideQuad(self): 
        
        if len(self.subdivisionMemory)-1>self.subdivision_level: #if we have data in cache take it from cache
            self.points=self.subdivisionMemory[self.subdivision_level+1]
        else:               
            self.points=self.divideQuadSurface() # if we dont have data go and calculate it, also put new data to the cache
            
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
        
        self.subdivision_level+=1
    
    def divideTriangle(self): 
        
        if len(self.subdivisionMemory)-1>self.subdivision_level: #if we have data in cache take it from cache
            self.points=self.subdivisionMemory[self.subdivision_level+1]
        else:               
            self.points=self.divideTriangleSurface() # if we dont have data go and calculate it, also put new data to the cache
            
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
        
        self.subdivision_level+=1
    
    #----------------------------------------------------------------------------------
    #BELOW IS CODE USED FOR CATMULL CLARK SUBDIVISON. OLD HOMEWORKS USED ABOVE CODE
    #----------------------------------------------------------------------------------
    
    def subdivide(self):
        
        if len(self.subdivisionMemory)-1>self.subdivision_level: #if we have data in cache take it from cache
            self.points=self.subdivisionMemory[self.subdivision_level+1]
        else:               
            points=self.get_points_from_faces(self.catmull()) # if we dont have data go and calculate it, also put new data to the cache
            self.subdivisionMemory.append(points)
            self.points=points
            
        self.matrix=self.get_matrix(self.points)
        self.center=self.get_center(self.points)
        self.apply_transformation_matrix()
        
        self.subdivision_level+=1
    
    def catmull(self):
        self.meshMemory.append(Mesh(self.vertexTable,self.edgeTable,self.faceTable))
        
        newFaceTablePositions=[]
        
        vertexTable=[]
        faceTable=[]
        edgeTable=[]
        
        for faceObj in self.faceTable:
            new_faces=self.findNewFacesFromFace(faceObj) #position list
            
            for facePos in new_faces:
            
                v1=Vertex(facePos[0])
                v2=Vertex(facePos[1])
                v3=Vertex(facePos[2])
                v4=Vertex(facePos[3])
                
                vertexTable.extend([v1,v2,v3,v4])
                
                v1=self.getVertexFromTheTable(v1,vertexTable)
                v2=self.getVertexFromTheTable(v2,vertexTable)
                v3=self.getVertexFromTheTable(v3,vertexTable)
                v4=self.getVertexFromTheTable(v4,vertexTable)
                    
            
                face=Face([v1,v2,v3,v4])
            
                v1.addFace(face)
                v2.addFace(face)
                v3.addFace(face)
                v4.addFace(face)
            
                edge1=Edge(v1,v2)
                edge2=Edge(v2,v3)
                edge3=Edge(v3,v4)
                edge4=Edge(v1,v4)
                    
                v1.addEdge(edge1,edge4)
                v2.addEdge(edge1,edge2)
                v3.addEdge(edge2,edge3)
                v4.addEdge(edge3,edge4)
                
                
                faceTable.append(face)
                edgeTable.append(edge1)
                edgeTable.append(edge2)
                edgeTable.append(edge3)
                edgeTable.append(edge4)
            
            
            
            newFaceTablePositions.extend(new_faces)
        

        
        
        self.faceTable=faceTable
        self.edgeTable=edgeTable
        self.vertexTable=vertexTable
        
        return newFaceTablePositions
    
    def findNewFacesFromFace(self,faceObj):
        facePoint=faceObj.getFacePoint()
            
            #-------------
            
        vertexObjList=faceObj.vertices
        
        v1=vertexObjList[0]
        v2=vertexObjList[1]
        v3=vertexObjList[2]
        v4=vertexObjList[3]
        
        v1_new=self.findNewPointFromVertex(v1)
        v2_new=self.findNewPointFromVertex(v2)
        v3_new=self.findNewPointFromVertex(v3)
        v4_new=self.findNewPointFromVertex(v4)
        
        edgePointsOfV1=self.findEdgePointsFromVertex(faceObj,v1)
        edgePointsOfV2=self.findEdgePointsFromVertex(faceObj,v2)
        edgePointsOfV3=self.findEdgePointsFromVertex(faceObj,v3)
        edgePointsOfV4=self.findEdgePointsFromVertex(faceObj,v4)
        
        face1=[v1_new,edgePointsOfV1[0],facePoint,edgePointsOfV1[1]]
        face2=[v2_new,edgePointsOfV2[0],facePoint,edgePointsOfV2[1]]
        face3=[v3_new,edgePointsOfV3[0],facePoint,edgePointsOfV3[1]]
        face4=[v4_new,edgePointsOfV4[0],facePoint,edgePointsOfV4[1]]
        
        return [face1,face2,face3,face4]
    
    def getVertexFromTheTable(self,aVertex,vertexTable):
        for vertex in vertexTable:
            if vertex.isEqual(aVertex):
                return vertex

        return aVertex
    
    def findNewPointFromVertex(self,vertex):
        adjFacesOfVertex=vertex.adjFaces
        facePointList=[]
        for face in adjFacesOfVertex:
            facePointList.append(face.facePoint)
        avgFacePoints=self.getAvg(facePointList)
                
        adjEdgesOfVertex=vertex.adjEdges
                
        edgeMidPointList=[]
        for edge in adjEdgesOfVertex:
            edgeMidPointList.append(edge.middlePoint)
        avgEdgeMidPoints=self.getAvg(edgeMidPointList)
                
        oldVertexPos=vertex.position
        
        newPoint=self.baryCenter(avgFacePoints,avgEdgeMidPoints,oldVertexPos)
        
        return newPoint
    
    def findEdgePointsFromVertex(self,faceObj,vertex):
        adjEdgesOfVertex=vertex.adjEdges
        
        edgesInsideFace=[]
        for edg in adjEdgesOfVertex:
            if self.isEdgeInsideFace(faceObj,edg):
                edgesInsideFace.append(edg)

                
        edgePoints=[edgesInsideFace[0].getEdgePoint(),edgesInsideFace[1].getEdgePoint()]
        return edgePoints
    
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
    
    def baryCenter(self,F,R,P):
        n=self.cornerNumber
    
        Rcoefficent=2/n
        Pcoefficent=(n-3)/n
        Fcoefficent=1/n
        
        Rtotal=R.multiply(Rcoefficent)
        Ftotal=F.multiply(Fcoefficent)
        Ptotal=P.multiply(Pcoefficent)
        
        temp=Rtotal.add(Ftotal)
        addition=temp.add(Ptotal)
        
        return addition
    
    def isEdgeInsideFace(self,faceObj,edgeObj):
        edgeVertices=edgeObj.vertices
        
        vertex1=edgeVertices[0]
        vertex2=edgeVertices[1]
        
        in1=faceObj.isVertexInside(vertex1)
        in2=faceObj.isVertexInside(vertex2)
        
        if in1==True and in2==True:
            return True
        else:
            return False
        
    