#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s_one = {}
    for i in s1:
        s_one[i] = 1
    for i in s2:
        if i in s_one:
            return 1
    return 0


if __name__ == '__main__':

    q = int(input())
    arr = []
    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        arr.append(result)
    for i in arr:
        if i == 0:
            print("NO")
        else:
            print("YES")
