if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    temp = arr[n-1]
    for i in arr[::-1]:
        if(i!=temp):
            temp = i
            break
    print temp
