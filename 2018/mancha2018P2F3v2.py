def checar_linear(linha):
    estado = 0
    
    for sq in linha:
        if sq == '*' and estado == 0:
            estado = 1
        elif sq == '.' and estado == 1:
            estado = 2
        elif sq == '*' and estado == 2:
            return True
    return False

def detectar_buracos(matriz, n):
    for i in range(n): # Por linhas
        if checar_linear(matriz[i]):
            return True

    for j in range(n): # Por colunas
        if checar_linear([matriz[i][j] for i in range(n)]):
            return True
    
    return False

n = int(input())
matriz = [list(input()) for _ in range(n)]

if detectar_buracos(matriz, n):
    print('N')

else:
    print('S')
