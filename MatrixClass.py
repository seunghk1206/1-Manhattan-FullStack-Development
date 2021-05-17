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
    
def MagicSquare(dimension):
    initInd = random.randint(1, dimension)
    print(initInd)
    for i in range(dimension**2):
        pass
MagicSquare(5)
matrix1 = matrix([[1,2,3], [1,2,0]])
matrix2 = [[0, 5], [1, 2], [3, 4]]
print(matrix1.MultiplyMatrix(matrix2))
print(matrix1.TransposeMatrix())
matrix1 = matrix([[1,2,3], [1,2,0], [1,3,2]])
print(matrix1.Diagonals())