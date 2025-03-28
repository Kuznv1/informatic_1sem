n, m, k = map(int, input().split())
graph = [i for i in range(1, n + 1)]
R = [0] * n

for _ in range(m):
    input()

Operations = [input() for _ in range(k)]
Operations = reversed(Operations)

def Find(A, b):
    if A[b-1] != b:
        A[b-1] = Find(A, A[b-1])
    return A[b-1]

def Uni(A, B, x, y):
    x = Find(A, x)
    y = Find(A, y)
    if x == y:
        return
    if B[x-1] == B[y-1]:
        B[x-1] += 1
    if B[x-1] < B[y-1]:
        A[x-1] = y
    else:
        A[y-1] = x




answ = []
for operation in Operations:
    action, x, y = operation.split()
    x, y = int(x), int(y)

    if action == 'ask':
        answ.insert(0, 'YES' if Find(graph, x) == Find(graph, y) else 'NO')
    
    if action == 'cut':
        Uni(graph, R, x, y)

print('\n'.join(answ))