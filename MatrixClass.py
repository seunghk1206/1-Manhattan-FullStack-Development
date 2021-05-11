class matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def TransposeMatrix(self):
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

matrix1 = matrix([[1,2,3], [1,2,0]])
matrix2 = [[0, 5], [1, 2], [3, 4]]
print(matrix1.MultiplyMatrix(matrix2))
print(matrix1.TransposeMatrix())