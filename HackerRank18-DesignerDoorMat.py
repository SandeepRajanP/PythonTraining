# Enter your code here. Read input from STDIN. Print output to STDOUT
NM = raw_input().split()
N = int(NM[0])
M = int(NM[1])

for i in range(N/2):
    print "-"*((M-3*(1+2*i))/2)+".|."*(1+2*i)+"-"*((M-3*(1+2*i))/2)
print "-"*((M-7)/2)+"WELCOME"+"-"*((M-7)/2)   
for i in range(N/2):
    print "-"*((M-3*(N-2*(1+i)))/2)+".|."*(N-2*(1+i))+"-"*((M-3*(N-2*(1+i)))/2)
