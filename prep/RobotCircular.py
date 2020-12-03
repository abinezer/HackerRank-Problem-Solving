#!/bin/python3
'''
Given a sequence of moves for a robot, check if the sequence is circular or not. A sequence of moves is circular if first and last positions of robot are same. A move can be on of the following.
    
    G - Go one unit
    L - Turn left
    R - Turn right

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is a String in capital letter, sequence of moves consisting only {R,G,L}.

Output:

Print Given sequence of moves is circular if first and last positions of robot are same. else Given sequence of moves is NOT circular.
'''
import math
import os
import random
import re
import sys

def Circular(q):
    x = 0
    y = 0

    # let +x direction be +1 and +y direction be +2

    direction = 2

    for i in q:
        if i == 'G':
            if direction == 2 or direction == -2:
                y = y + direction 
            elif direction == 1 or direction == -1:
                x = x + direction
        elif i == 'L':
            if direction == 2:
                direction = -1
            elif direction == -2:
                direction = 1
            elif direction == 1:
                direction = 2
            elif direction == -1:
                direction = -2
        elif i == 'R':
            if direction == 2:
                direction = 1
            elif direction == -2:
                direction = -1
            elif direction == 1:
                direction = -2
            elif direction == -1:
                direction = 2
    if x == 0 and y == 0:
        return 1
    else:
        return -1




if __name__ == '__main__':
    t = int(input())
    soln = []
    for t_itr in range(t):

        q = input()

        result = Circular(q)
        soln.append(result)
    
    for j in soln:
        if j == -1:
            print("Not Circular")
        else:
            print("Circular")