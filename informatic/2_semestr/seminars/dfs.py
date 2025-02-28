graph = {0:[1,4], 1:[3,5], 2:[3], 3:[], 4:[2], 5:[]}
#graph = {0:[1,4], 1:[2,3], 2:[3], 3:[0], 4:[1]}

color = ['white' for i in range(len(graph.keys()))]

'''def dfs_visit(graph, v):
    color[v] = 'gray'
    print(v)

    for u in graph[v]:
        if color[u] == 'white':
            dfs_visit(graph, u)

        color[v] == 'black'
#print(color)
dfs_visit(graph, 0)
либо я туплю, либо код нерабочий'''

stack = [0]

while stack:
    node = stack.pop()
    app = 0

    if color[node] == 'white':
                print(node)
                color[node] = 'gray' 

    if len(graph[node]) == 0:
        color[node] = 'black'
        
    else:
        for i in graph[node]:
            if color[i] == 'white':
                stack.append(i)
                app += 1
        if app == 0:
            color[node] = 'black'
    
print(color)
           
#dex с весами          


             

    
       