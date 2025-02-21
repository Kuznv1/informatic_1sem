#4
f = open('input.txt', 'r')
F = []
for line in f:    
    F += line.split() 
    
print(F)
Zn = F.pop()
A = []
#print(Zn, A)
for i in F:
    A.append(int(i))
    

n = len(A)
b = 0
#print(A)
if Zn == '+':
    for k in A:
        b += k
elif Zn == '-':
    b = A[0]
    for k in range(1, n+1):
        b -= A[k]
if Zn == '*':
    b = 1
    for k in A:
        b *= k
f2 = open('output.txt', 'w')
f2.write(str(b))
f.close()
f2.close()
