def rotar_matriz(matriz, N):
    nova_matriz = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            nova_matriz[j][N-1 - i] = matriz[i][j]
    
    return nova_matriz

def detectar_buracos(matriz, N):
    for linha in matriz:
        a = False

        for i in range(N-1):
            if linha[i] == '*' and linha[i+1] == '.' and not a:
                a = True
                continue
                
            if linha[i] == '*' and a:
                return True
                
    return False

N = int(input())
mancha = [list(input()) for _ in range(N)]

a = detectar_buracos(mancha, N) # Horizontal

if a:
    print('N')
else:
    mancha = rotar_matriz(mancha, N)
    b = detectar_buracos(mancha, N) # Vertical
    if b:
        print('N')
    else:
        print('S')