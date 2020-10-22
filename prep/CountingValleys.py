#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    stack = []
    flag = -1
    valleys = 0
    for i in range(steps):
        if (path[i] == 'U' and len(stack) == 0):
            stack.append(0)
            flag = 0
        elif (path[i] == 'D' and len(stack) == 0):
            stack.append(1)
            flag = 1
        elif (path[i] == 'D' and flag == 0):
            stack.pop()
        elif (path[i] == 'U' and flag == 0):
            stack.append(1)
        elif (path[i] == 'D' and flag == 1):
            stack.append(1)
        elif (path[i] == 'U' and flag == 1):
            stack.pop()
        if(flag == 1 and len(stack) == 0):
            valleys = valleys + 1
    return valleys

if __name__ == '__main__':
    fptr = sys.stdout

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

