#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i = 0
    flag = 0
    while(i < n-1):
        if c[i+1] == 1 :
            jumps = jumps + 1
            i = i + 2
            flag = 0
        elif c[i+1] == 0:
            i = i + 1
            jumps = jumps + 1
            flag = flag + 1
        if flag == 2:
            flag = 0
            jumps = jumps - 1
    return jumps
if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
