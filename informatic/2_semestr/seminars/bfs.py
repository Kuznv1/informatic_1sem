graph = {0:[1,4], 1:[2,3], 2:[3], 3:[0], 4:[1]}

def bfs(graph, start):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node)        

        for neighboor in graph[node]:
            if neighboor not in visited:
                queue.append(neighboor)
                visited.add(neighboor)

#DSP

#dfs