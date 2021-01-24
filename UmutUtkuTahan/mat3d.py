#CENG487 Assignment1 by
#Umut Utku Tahan
#250201086
#January 2020

import math

class Mat3d:
    
    
    def __init__(self,lst):
        self.lst=lst
    
    def matrixMul(self,matrix):

        if len(self.lst[0])==len(matrix.lst):
        
            result = [[sum(a * b for a, b in zip(A_row, B_col))  
                            for B_col in zip(*matrix.lst)] 
                                    for A_row in self.lst] 
      
           
            return Mat3d(result)
        else:   
            print("invalid matrices given for multiplication")
            
            
    def transpose(self):
        result = [[self.lst[j][i] for j in range(len(self.lst))] for i in range(len(self.lst[0]))]

        
        return Mat3d(result)

    def mulVec(self,Vec3d):
        vec=[[Vec3d.x],[Vec3d.y],[Vec3d.z],[Vec3d.w]]
        
        return self.matrixMul(vec)
    @staticmethod
    def get_translation_matrix(trans_x,trans_y,trans_z):
        return Mat3d([[1,0,0,trans_x],[0,1,0,trans_y],[0,0,1,trans_z],[0,0,0,1]])
    @staticmethod
    def get_scale_matrix(scalar):
        return Mat3d([[scalar,0,0,0],[0,scalar,0,0],[0,0,scalar,0],[0,0,0,scalar]])
    @staticmethod
    def get_rotation_matrix_x_axis(Q):
        return Mat3d([[1,0,0,0],[0,math.cos(math.radians(Q)),-math.sin(math.radians(Q)),0],
                      [0,math.sin(math.radians(Q)),math.cos(math.radians(Q)),0],[0,0,0,1]
                      ])
    @staticmethod
    def get_rotation_matrix_y_axis(Q):
        return Mat3d([[math.cos(math.radians(Q)),0,math.sin(math.radians(Q)),0],[0,1,0,0],
                      [-math.sin(math.radians(Q)),0,math.cos(math.radians(Q)),0],[0,0,0,1]
                      ])
    @staticmethod
    def get_rotation_matrix_z_axis(Q):
        return Mat3d([[math.cos(math.radians(Q)),-math.sin(math.radians(Q)),0,0],
                      [math.sin(math.radians(Q)),math.cos(math.radians(Q)),0,0],[0,0,1,0],[0,0,0,1]
                      ])
    def transposeMatrix(self,m):
        return Mat3d(map(list,zip(*m.lst)))

    def getMatrixMinor(self,m,i,j):
        return Mat3d([row[:j] + row[j+1:] for row in (m.lst[:i]+m.lst[i+1:])])
    
    def getMatrixDeternminant(self,m):
        #base case for 2x2 matrix
        if len(m.lst) == 2:
            return m.lst[0][0]*m.lst[1][1]-m.lst[0][1]*m.lst[1][0]
    
        determinant = 0
        for c in range(len(m.lst)):
            determinant += ((-1)**c)*m.lst[0][c]*self.getMatrixDeternminant(self.getMatrixMinor(m,0,c))
        return determinant
    
    def getMatrixInverse(self,m):
        determinant = self.getMatrixDeternminant(m)
        #special case for 2x2 matrix:
        if len(m.lst) == 2:
            return [[m.lst[1][1]/determinant, -1*m.lst[0][1]/determinant],
                    [-1*m.lst[1][0]/determinant, m.lst[0][0]/determinant]]
    
        #find matrix of cofactors
        cofactors = []
        for r in range(len(m.lst)):
            cofactorRow = []
            for c in range(len(m.lst)):
                minor = self.getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * self.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors=Mat3d(cofactors).transpose().lst
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors
    


        
        