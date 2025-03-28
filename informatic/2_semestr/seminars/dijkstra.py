G = {0: {1: 1.5, 4: 0.5}, 1:{2:1, 3:3}, 2:{3:1}, 3:{0:2}, 4: {1: 0.5}, 5:{4:1}}

# Поиск кратчайшего пути

def Dijkstra(G,s):
    V = len(G.keys())
    dist = [float('inf') for i in range(V)]
    prev = [None for i in range(V)]
    dist[s] = 0
    prev[s] = 0
    S = set()
    n = 0
    while len(S) < V and n != V:
        v = dist.index(min(dist))

        S.add(v)
        #dist[v] = float('inf')
        for u, w in G[v].items():
            if u not in S and dist[u] > dist[v] + w:
                prev[u] = dist[v] + w
                dist[u] = dist[v] + w                
                #print(dist, v, u, S, n, prev)
        dist[v] = float('inf')
        n +=1

        
    return prev

print(Dijkstra(G, 0))


