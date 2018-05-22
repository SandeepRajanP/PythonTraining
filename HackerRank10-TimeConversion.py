#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    l = s.split(":")
    if l[2][2:4] == "PM":
        l[0] = str(int(l[0])+12)
        if int(l[0]) == 24:
            l[0] = "12"
    elif l[2][2:4] == "AM":
        if int(l[0]) == 12:
            l[0] = "00"        
    return (l[0]+":"+l[1]+":"+l[2][0:2])
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
