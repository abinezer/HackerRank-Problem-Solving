#!/bin/python3

import math
import os
import random
import re
import sys


def ZigZag(string, k):
    u = k
    k = (k*2) - 2
    s = k
    flag = 0
    for i in range(u):
        #i = 0
        a = k - s
        flag = 0
        for j in range(i):
            print(' ', end = '')
        j = i
        while(j < len(string) and s >= 0):
            if (s == k or s == 0) and (flag == 0):
                switchvar = k
            elif flag == 0 and s != k and s!= 0:
                switchvar = s
                flag = 1
            else:
                switchvar = a
                flag = 0
            print(string[j], end = '')
            for t in range(1,switchvar):
                print(' ', end = '')
            j = j + switchvar
        print('\n', end = '')
        s = s - 2

if __name__ == '__main__':
    fptr = sys.stdout

    string = input()

    k = int(input())

    ZigZag(string,k)

    #fptr.write(str(result) + '\n')

    fptr.close()