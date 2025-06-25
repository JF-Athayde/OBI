def encontrar_posicao_final(l, c, a, b, matriz):
    direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x, y = a - 1, b - 1
    
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if 0 <= nx < l and 0 <= ny < c and matriz[nx][ny] == 1:
            dir_x, dir_y = dx, dy
            break
    else:
        return a, b
    
    while 0 <= x + dir_x < l and 0 <= y + dir_y < c and matriz[x + dir_x][y + dir_y] == 1:
        x += dir_x
        y += dir_y
    
    return x + 1, y + 1 

L, C = map(int, input().split())
A, B = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(L)]

resultado = encontrar_posicao_final(L, C, A, B, matriz)
print(resultado[0], resultado[1])
