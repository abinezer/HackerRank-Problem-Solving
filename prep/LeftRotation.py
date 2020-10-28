#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    BigArray = []
    for t in range(0,2*n):
        if t < n:
            BigArray.append(a[t])
        else:
            BigArray.append(0)
    numberOfRotations = d % n
    i = 0
    RotatedArray = []
    while(i < numberOfRotations):
        BigArray[n + i] = a[i]
        i = i + 1
    j = numberOfRotations
    while(j < numberOfRotations + n):
        RotatedArray.append(BigArray[j])
        j = j + 1
    return RotatedArray


if __name__ == '__main__':
    fptr = sys.stdout

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
