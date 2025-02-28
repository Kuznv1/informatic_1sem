graph = {0:[1, 4], 1:[2,3], 2:[3], 3:[0], 4:[1], 5:[0]}

# top sort
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


#dfs
def dfs_visit(graph, node, color, visited):
    color[node] = 1
    visited.append(node)
    for neigbour in graph[node]:
        if color[neigbour] == 0:
            dfs_visit(graph, neigbour, color, visited)

    color[node] == 2

def dfs_recoursive(graph):
    components = []
    color = [0 for _ in graph]
    for node in graph:
        if color[node] == 0:
            visited = []
            dfs_visit(graph, node, color, visited)
            components.append(visited)
    return components

def kosaraju(graph):
    # 1 топсортировка
    top_sort = topological_sort(graph)
    # 2 трвнспонирование графа
    graph_t = {node: [] for node in graph}
    for node in graph:
        for neigbour in graph[node]:
            graph_t[neigbour].append(node)
    
    color = [0 for _ in graph]    

    while top_sort:
        node = top_sort[0]       
        component = []
        dfs_visit(graph_t, node, color, component)
        print(component)
        for node in component:  
            top_sort.remove(node)
            
kosaraju(graph)