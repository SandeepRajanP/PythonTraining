#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    x = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zero += 1
    print(pos/x)
    print(neg/x)
    print(zero/x)           
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
