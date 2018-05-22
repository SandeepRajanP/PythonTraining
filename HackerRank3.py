#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    A = 0
    B = 0
    for i in range(len(a)):
        if a[i]>b[i] :
            A=A+1
        elif a[i] < b[i] :
            B=B+1
        else:
            A = A 
            B = B
    return A,B
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
