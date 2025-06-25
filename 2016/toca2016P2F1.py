def bfs(matriz, inicio, destino, linhas, colunas):
    fila = [(inicio[0], inicio[1], 1)]
    visitados = set([inicio])
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        x, y, distancia = fila.pop(0)

        if (x, y) == destino:
            return distancia
        
        for dx, dy in movimentos:
            nx, ny = x+dx, y+dy

            if 0 <= nx < linhas and 0 <= ny < colunas and matriz[nx][ny] != 0 and (nx, ny) not in visitados:
                fila.append((nx, ny, distancia+1))
                visitados.add((nx, ny))
    return -1

def buscar_inicio_fim(matriz, inicio, fim):
    inicio_ = (None, None)
    fim_ = (None, None)

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == inicio:
                inicio_ = (i, j)
            if matriz[i][j] == fim:
                fim_ = (i, j)
            
            if inicio_ != (None, None) and fim_ != (None, None):
                return inicio_, fim_
    return -1

n, m = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(n)]

inicio, fim = buscar_inicio_fim(matriz, 2, 3)
print(bfs(matriz, inicio, fim, n, m))
