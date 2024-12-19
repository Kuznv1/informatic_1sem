B=[]
c = 2
D = 3
while D >= c:
    B.append(D%c)
    D = D//c
if D !=0:
    B.append(D)
print(B)