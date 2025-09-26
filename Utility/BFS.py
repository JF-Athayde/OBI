def bfs(matriz, start, end, L, C):
    fila = []
    visited = [[False] * C for _ in range(L)]

    fila.append((start[0], start[1], 0))  # L, C, steps

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while fila:
        x, y, steps = fila.pop(0)

        if matriz[x][y] == end:
            return steps

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0 <= nx < L and 0 <= ny < C:
                if not visited[nx][ny] and (matriz[nx][ny] == 0 or matriz[nx][ny] == end):
                    visited[nx][ny] = True
                    fila.append((nx, ny, steps + 1))
    return -1

matriz = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 2, 1, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
L, C = 4, 4

print(bfs(matriz, start, 2, L, C))
