#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def summateHourGlass(glassArr):
    retL = []
    sumNum = 0
    for i in range(1, len(glassArr)-1):
        for j in range(1, len(glassArr[0])-1):
            sumNum += glassArr[i][j]
            sumNum += glassArr[i-1][j-1]
            sumNum += glassArr[i-1][j+1]
            sumNum += glassArr[i+1][j-1]
            sumNum += glassArr[i+1][j+1]
            sumNum += glassArr[i-1][j]
            sumNum += glassArr[i+1][j]
            retL.append([sumNum, i, j])
            sumNum = 0
    return retL

def hourglassSum(arr):
    SumL = summateHourGlass(arr)
    sumL = [each[0] for each in SumL]
    return max(sumL)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()