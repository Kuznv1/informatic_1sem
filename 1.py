from collections import deque

def topological_sort_unique(n, edges):
    # Строим граф и считаем степени вершин
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Инициализируем очередь для вершин с нулевой степенью
    zero_in_degree = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            zero_in_degree.append(i)

    count = 0
    unique = True

    while zero_in_degree:
        if len(zero_in_degree) > 1:  # Если больше одной вершины с нулевой степенью
            unique = False
        
        current = zero_in_degree.popleft()
        count += 1

        # Уменьшаем степень соседей
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    # Если обработано не все вершины, значит есть цикл
    if count < n:
        return -1
    
    return "YES" if unique else "NO"

# Чтение входных данных
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = topological_sort_unique(n, edges)
print(result)
