def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)

def bfs(matriz, inicio, linhas, colunas, quadrante):
    matriz_atualizada = matriz.copy()

    fila = [inicio]
    visitados = set([inicio])

    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while fila:
        x, y = fila.pop(0)
        
        matriz_atualizada[x][y] = quadrante

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy

            if (0 <= nx < linhas and
                0 <= ny < colunas and
                (nx, ny) not in visitados and
                matriz[nx][ny] != 0):

                fila.append((nx, ny))
                visitados.add((nx, ny))

    return matriz_atualizada

linhas, colunas = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(linhas)]

cont = 2
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == 1:
            matriz = bfs(matriz, (i, j), linhas, colunas, cont)
            cont += 1

print(cont-2)