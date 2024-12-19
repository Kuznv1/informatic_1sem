N, base, c = input().split()
base = int(base)
c = int(c)
A = []
k = 1

D = 0


if base != 10:
    for i in N:
        A.append(int(i))
    

    n = len(A)-1
    for i in A:
        D += i*(base**n)
        n -= 1
else:
    D = N



B=[]
while D >= c:
    B.append(D%c)
    D = D//c
if D !=0:
    B.append(D)

B.reverse()

M = ''
for r in B:
    M = M + str(r)


print(M)