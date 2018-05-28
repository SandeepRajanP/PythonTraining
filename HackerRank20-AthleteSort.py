#!/bin/python



if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))
    k = int(raw_input())
    l = sorted(arr,key=lambda x:x[k])
    for i in l:
        print(" ".join(map(str, i)))
    
