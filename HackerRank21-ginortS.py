# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input()
alpha = ""
beta = ""
gamma = ""
delta = ""
for char in s:
    if char.isalpha() and char.isupper()!= True:
        alpha = alpha+ char
alpha = sorted(alpha) 
alpha = "".join(alpha)
for char in s:
    if char.isalpha() and char.isupper() == True:
        beta = beta + char
beta = sorted(beta) 
beta = "".join(beta)        
for char in s:
    if char.isdigit():
        if int(char)%2 != 0:
            gamma = gamma + char
gamma = sorted(gamma) 
gamma = "".join(gamma)
for char in s:
    if char.isdigit():
        if int(char)%2 == 0:
            delta = delta + char
delta = sorted(delta) 
delta = "".join(delta)
print alpha+beta+gamma+delta
