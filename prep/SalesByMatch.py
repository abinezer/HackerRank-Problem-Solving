#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    count = 0
    i = 0
    t = n
    while(t):
        if i == n-1:
            t = t - 1
        elif ar[i] == ar[i+1]:
            count = count + 1
            i = i + 2
            t = t - 2
        else:
            i = i + 1
            t = t - 1
    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

