from hashlib import new

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

a = list(map(int, input().split()))
inpL = []
def game(a, inpL):
    for _ in a[0]:
        inpL.append(list(map(int, input().split())))

    matL = matrix(inpL)
    TL = matL.TransposeMatrix()
    tempL = []

    for each in TL:
        tempL.append(min(each))

    ret = tempL.index(max(tempL))
    return ret

print(game(a, inpL))