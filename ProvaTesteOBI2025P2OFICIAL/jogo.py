def vizinhas_vivas(i, j, matriz, n):
    vizinhos = 0
    for dx, dy in [(-1, 0), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1)]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < n and 0 <= nj < n and matriz[ni][nj] == 1:
            vizinhos += 1
    return vizinhos

def gerar(matriz, n):
    nova = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            vivos = vizinhas_vivas(i, j, matriz, n)
            if matriz[i][j] == 1 and vivos in (2, 3):
                nova[i][j] = 1
            elif matriz[i][j] == 0 and vivos == 3:
                nova[i][j] = 1
    return nova

n, q = map(int, input().split())
matriz = [list(map(int, input().strip())) for _ in range(n)]

for _ in range(q):
    matriz = gerar(matriz, n)

for linha in matriz:
    print(''.join(map(str, linha)))
