#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    A = 0
    B = 0
    for i in range(len(a)):
        A += a[i][i]
    for i in range(len(a)):
        B += a[i][len(a)-i-1]
    return abs(A - B)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
