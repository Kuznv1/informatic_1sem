n, m = map(int, input().split())
deg = [0 for _ in range(n + 1)]
graph = {}

for _ in range(m):
    s, f =  map(int, input().split())
    if s not in graph:
        graph[s] = []
    graph[s].append(f)
    deg[f] += 1 #степени входящих
for v in range(1, n+1):
    if v not in graph:
        graph[v] = [0]

queue_zero = []
for i in range(1, n+1): 
    if deg[i] == 0:
        queue_zero.append(i)
stop = 1
nodes = 0
while queue_zero:
    if len(queue_zero) > 1:
        stop = 0
    nodes += 1
    now = queue_zero.pop(0)
    #print(now, graph)
    for nb in graph[now]:
        if nb != 0:
            deg[nb] -= 1
            if deg[nb] == 0:
                queue_zero.append(nb)

if n > nodes:
    print(-1)
else:
    if stop == 1:
        print('YES')
    else:
        print('NO') 




