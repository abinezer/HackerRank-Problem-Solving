#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    for i in s:
        if i == 'a':
            count = count + 1
    iterations = math.floor(n/len(s))
    numberOfA = count * iterations
    mod1 = n % len(s)
    for i in range(mod1):
        if s[i] == 'a':
            numberOfA = numberOfA + 1
    return numberOfA

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
