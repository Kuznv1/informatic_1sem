a, b = map(int, input().split())

Map = [[0 for j in range(b)] for i in range(a)]

Map[0][0] = 1

if a >= 3 and b >= 2:
    Map[2][1] = 1
 
if a >= 2 and b >= 3:
    Map[1][2] = 1


for i1 in range(1, a):
    for j1 in range(1, b):
        Map[i1][j1] = Map[i1-2][j1-1] + Map[i1-1][j1-2]
        

print(Map[a-1][b-1])

