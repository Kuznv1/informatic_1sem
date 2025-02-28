graph = {0:[1, 4], 1:[2,3], 2:[3], 3:[0], 4:[1], 5:[0]}

#0 - white, 1- gray, 2 - black

def dfs_visit(graph, node, color):
    color[node] = 1
    print(node)

    for neigbour in graph[node]:
        if color[neigbour] == 0:
            dfs_visit(graph, neigbour, color)

    color[node] == 2

def dfs_recoursive(graph):
    color = [0 for _ in graph]
    for node in graph:
        if color[node] == 0:
            dfs_visit(graph, node, color)

    
#print(color)
#dfs_recoursive(graph)

def topological_sort_visit(graph, node, color, top_sort):
    color[node] = 1

    for neigbour in graph[node]:
        if color[neigbour] == 0:
            topological_sort_visit(graph, neigbour, color, top_sort)

    color[node] == 2
    top_sort.insert(0, node)


def topological_sort(graph):
    color = [0 for _ in graph]
    top_sort = []
    for node in graph:
        if color[node] == 0:
            topological_sort_visit(graph, node, color, top_sort)
    return top_sort

#print(topological_sort(graph))