from hashlib import new
import random
class matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def TransposeMatrix(self):
        if len(self.matrix) == len(self.matrix[0]):
            TransposeMatrix = []
            tempL = []
            for i in range(len(self.matrix[0])):
                for j in range(len(self.matrix)):
                    tempL.append(self.matrix[j][i])
                TransposeMatrix.append(tempL)
                tempL = []
            return TransposeMatrix
    def AddMatrix(self, additionalMatrix):
        tempL = []
        retL = []
        if len(additionalMatrix) == len(self.matrix) and len(additionalMatrix[0]) == len(additionalMatrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    tempL.append(self.matrix[i][j] + additionalMatrix[i][j])
                retL.append(tempL)
                tempL = []
            return retL
    def Diagonals(self):
        tempL = []
        temp2L = []
        for i in range(len(self.matrix)):
            tempL.append(self.matrix[i][i])
            temp2L.append(self.matrix[i][-i-1])
        return [tempL, temp2L]
    def MultiplyMatrix(self, multiplicationMatrix):
        var = 0
        tempL = []
        retL = []
        if len(self.matrix[0]) == len(multiplicationMatrix):
            for i in range(len(multiplicationMatrix[0])):
                print(i)
                for j in range(len(self.matrix)):
                    for l in range(len(self.matrix[0])):
                        var += self.matrix[j][l]*multiplicationMatrix[l][i]
                    tempL.append(var)
                    var = 0
                retL.append(tempL)
                tempL = []
            return retL

def MagicIndex(a, dim):
    return [a//dim, a%dim-1]


# 5->2
# 7->3
def MagicSquare(dimension):
    if dimension%2 == 1:
        initInd = MagicIndex(dimension**2-dimension//2, dimension)
        initL = [[0 for _ in range(dimension)] for _ in range(dimension)]
        initL[initInd[0]][initInd[1]] = 1
        newInd = initInd
        for i in range(dimension**2-1):
            if newInd[0]+1 >= dimension:
                rightDownInd = [(newInd[0]+1)%dimension, (newInd[1]+1)%dimension]
            else:
                rightDownInd = [(newInd[0]+1)%dimension, (newInd[1]+1)%dimension]
            if initL[rightDownInd[0]][rightDownInd[1]] == 0:
                initL[rightDownInd[0]][rightDownInd[1]] = i+2
                newInd = rightDownInd
            else:
                if newInd[0] == 0:
                    newInd = [dimension-1, newInd[1]]
                else:
                    newInd = [newInd[0]-1, newInd[1]]
                initL[newInd[0]][newInd[1]] = i+2
        return initL
print(MagicSquare(5))
matrix1 = matrix([[1,2,3], [1,2,0]])
matrix2 = [[0, 5], [1, 2], [3, 4]]
print(matrix1.MultiplyMatrix(matrix2))
print(matrix1.TransposeMatrix())
matrix1 = matrix([[1,2,3], [1,2,0], [1,3,2]])
print(matrix1.Diagonals())