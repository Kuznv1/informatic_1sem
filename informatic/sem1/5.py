N, b, c = map(int, input().split())
A = []
k = 1

D = 0
 
if b != 10:
    while N >= 10:
        A.append(N%10)
        N = N//10
        k += 1
        A.append(N)

    n = 0
    for i in A:
        D += A[i]*(b**n)
        n += 1
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
    M = M + str(B[r])


print(M)