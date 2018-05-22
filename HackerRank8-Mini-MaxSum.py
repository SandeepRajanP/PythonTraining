#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
   
def miniMaxSum(arr):
    A = 0
    l = []
    x = len(arr)
    for i in range(x):
        A += arr[i]
    for j in range(x):
        l.append(A-arr[j])
    W = sorted(l);
    print(W[0],W[x-1])

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
