#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumList = []
    for i in range(4):
        topRow = i 
        for j in range(2,6):
            endColumn = j
            sumTopRow = arr[topRow][j-2] + arr[topRow][j-1] + arr[topRow][j]
            sumMiddle = arr[topRow+1][j-1]
            sumLowerRow = arr[topRow+2][j-2] + arr[topRow+2][j-1] + arr[topRow+2][j]
            s = sumTopRow + sumMiddle + sumLowerRow
            sumList.append(s)
    return max(sumList)

if __name__ == '__main__':
    fptr = sys.stdout
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
