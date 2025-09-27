def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    dist = [None] * n
    parent = [None] * n

    queue = [start]
    visited[start] = True
    dist[start] = 0

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    return dist, parent

graph = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2]
]

distances, parents = bfs(graph, 0)
print("Distâncias:", distances)
print("Pais:", parents)
