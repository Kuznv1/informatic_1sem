G = {0:{1:9, 4:11, 5:10}, 
     1:{0:9, 4:6, 3:11, 2:8}, 
     2:{1:8, 3:7}, 
     3:{2:7, 1:11, 4:2}, 
     4:{5:9, 0:11, 1:6, 3:2}, 
     5:{0:10, 4:9}}

def Prim(G):
    len_MST = 0 
    MST = []
    V = len(G.keys())
    dist = [float('inf') for i in range(V)]
    dist[0] = 0
    prev = [None for i in range(V)]
    S = set()
    
    while len(S) != V:
        v = dist.index(min(dist))
        S.add(v)
        if prev[v] is not None:
            MST.append([prev[v], v])

        for u, w in G[v].items():
            if u not in S and dist[u] > w:
                prev[u] = v
                dist[u] = w
        dist[v] = float('inf')
        
        #print(dist, prev, MST)

    for R in MST:
        len_MST += G[R[0]][R[1]]   
    

    return MST, len_MST
        
print(Prim(G))