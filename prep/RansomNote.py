#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag = {}
    for i in magazine:
        if i not in mag:
            mag[i] = 1
        else:
            mag[i] = mag[i] + 1
    for i in note:
        if i in mag and mag[i] != 0:
            mag[i] = mag[i] - 1
        else:
            return 0
    return 1

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    result = checkMagazine(magazine, note)
    if result:
        print("Yes")
    else:
        print("No")