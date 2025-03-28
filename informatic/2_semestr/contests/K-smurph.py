n, m = map(int, input().split())
smurphs = []
F = 0

for _ in range(m):
    stroka = input().split()
    I = int(stroka[0])
    r = int(stroka[1])
    k = int(stroka[2])
    zn = stroka[3]
    smurphs.append((I, r, k, zn))

D_rb = [float('inf') for i in range(n+1)]
D_rb[0] = 0
Versh = []

for I, r, k, zn in smurphs:
        if zn == '<=':
            Versh.append((I-1, r, k))
        elif zn == '>=':
            Versh.append((r, I-1, -k))

for _ in range(n + 1):

    for a, b, c in Versh:
        if D_rb[b] > c + D_rb[a] and D_rb[a] != float('inf'):
            D_rb[b] = c + D_rb[a]
            #print(D_rb, a, b, c)

Q = 0   
for a1, b1, c1 in Versh:
    
    if D_rb[b1] > c1 + D_rb[a1] and D_rb[a1] != float('inf'):
        F = 0
        Q = 1
        #print(D_rb)
if Q == 0:
    F = 1

if F == 0:
    print('NO')
else:
    print('YES')
        
