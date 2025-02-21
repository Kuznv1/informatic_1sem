graph = {0:[1,4], 1:[3,5], 2:[3], 3:[], 4:[2]}

color = ['white' for i in graph.keys()]

def dfs_visit(graph, v):
    color[v] = 'gray'
    print(v)

    for u in graph[v]:
        if color[u] == 'white':
            dfs_visit(graph, u)

        color[v] == 'black'
#print(color)
dfs_visit(graph, 0)