def func(N, a):
    dist = [float('inf')] * (N + 1)
    dist[0] = 0
    edges = []

    for l, r, k, sign in a:
        if sign == '>=':
            edges.append((r, l-1, -k))
        elif sign == '<=':
            edges.append((l-1, r, k))

    for i in range(N + 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            return False
    return True

N, M = map(int, input().split())
a = []
for i in range(M):
    parts = input().split()
    I = int(parts[0])
    r = int(parts[1])
    k = int(parts[2])
    sign = parts[3]
    a.append((I, r, k, sign))

print("YES" if func(N, a) else "NO")