#!/bin/python3

import math
import os
import random
import re
import sys

def kMF(s, k):
    freqOfLetters = {}
    arrOfFreq = []
    for i in s:
        if i in freqOfLetters:
            freqOfLetters[i] = freqOfLetters[i] + 1
        else:
            freqOfLetters[i] = 1
    
    for i in freqOfLetters:
        arrOfFreq.append(freqOfLetters[i])

    freq = [] 

    
    
    arrOfFreq = sorted(arrOfFreq)
    arrOfFreq = arrOfFreq[::-1]

    print(arrOfFreq)

    for i in arrOfFreq:
        if i not in freq:
            freq.append(i)

    print(freq)

    for i in freqOfLetters:
        if freqOfLetters[i] == freq[k-1]:
            return i
    
    return "Not found"






if __name__ == '__main__':
    fptr = sys.stdout

    string = input()

    k = int(input())

    result = kMF(string,k)

    fptr.write(str(result) + '\n')

    fptr.close()