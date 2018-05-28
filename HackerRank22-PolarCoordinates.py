# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath


a = raw_input()
for i in range(len(a)):
    if a[i]=='+':
        n,m = a.split('+')
        m = int(m[:len(m)-1])
        n = int(n)
    else:
        if a[i] == '-' and a[0]!='-' :
            n,m = a.split('-')  
            m = -1*int(m[:len(m)-1])
            n = int(n)
        elif a[0] == '-':
            try:
                n,m = a[1:].split('-')
                n = -1*int(n)        
                m = -1*int(m[:len(m)-1])
            except:
                n,m = a[1:].split('+')
                n = -1*int(n)        
                m = int(m[:len(m)-1])
x = cmath.phase(complex(n,m))
y = abs(complex(n,m))
print "%0.14f" % y
print "%0.14f" % x

