def conver_to(num, base):
    digits = list('0123456789abcdefghijklmnopqrstuvwxyz')
    if base > len(digits):
        return None
    result = str()
    while num > 0:
        result = digits[num % base] + result 
        num //= base
    return result

f = open("input.txt", 'r')
F = []
#f = open('input.txt', 'r')

for line in f:    
    F += line.split() 

base = int(F.pop())
zn = F.pop()
for i in F:
    i = int(i)

#print(F, zn, base)

D = []
if base != 10:
    for t in range(len(F)):
        A = []
        r = 0
        for i in F[t]:
            A.append(int(i))   

        n = len(A)-1
        for i in A:
            r += i*(base**n)
            n -= 1
        D.append(r)
else:
    for t in range(len(F)):
        D.append(int(F[t]))


b = 0

if zn == '+':
    for k in D:
        b += k
elif zn == '-':
    b = D[0]
    for k in range(1, n+1):
        b -= D[k]
elif zn == '*':
    b = 1
    for k in D:
        b *= D

f2 = open("output.txt", 'w')
f2.write(str(conver_to(b, base)))
f.close()
f2.close()

