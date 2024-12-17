def conver_to(num, base):
    digits = list('0123456789abcdefghijklmnopqrstuvwxyz')
    if base > len(digits):
        return None
    result = str()
    while num > 0:
        result = digits[num % base] + result 
        num //= base
    return result

f = open('input.txt', 'r')
F = []
for line in f:
    F.append(f.split())
A = list(F[0])
for i in A:
    A[i] = int(A[i])
zn = F[1]
base = int(F[2])

for i in A:
    D = 0 
    B = []
    if i != 10:
        while i >= 10:
            B.append(i % 10)
            i = i//10
        B.append(i)

        n = 0
        for i in B:
            D += B[i]*(base**n)
            n += 1

        i = D

b = 0

if zn == '+':
    for k in A:
        b += A[k]
elif zn == '-':
    b = A[0]
    for k in range(1, n+1):
        b -= A[k]
elif zn == '*':
    b = 1
    for k in A:
        b *= A[k]

f2 = open('output.txt', 'w')
f2.write(conver_to(b, base))
f.close()
f2.close()

