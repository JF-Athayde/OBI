def checar_igualdade(lista):
    if [lista[0]]*len(lista) == lista:
        return True
    return False

def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

def somar(quadrado):
    n = len(quadrado)
    somas = []

    # Soma linear
    for i in quadrado:
        somas.append(sum(i))
    
    # Soma colunar
    quadrado_transposto = []

    j = 0 # Linha
    k = 0 # Coluna

    linha = []
    while 0 <= k < n and 0 <= j < n:
        if j < n:
            linha.append(quadrado[j][k])
            j += 1
        if j == n:
            quadrado_transposto.append(linha.copy())
            linha.clear()

            k += 1
            j = 0

    for i in quadrado_transposto:
        somas.append(sum(i))
    
    # Soma diagonal 1
    diagonal01 = []

    j = 0 # Linha
    k = 0 # Coluna

    while 0 <= k < n and 0 <= j < n:
        diagonal01.append(quadrado[j][k])

        j += 1
        k += 1
    
    somas.append(sum(diagonal01))

    # Soma diagonal 2

    diagonal02 = []

    j = 0 # Linha
    k = n-1 # Coluna

    while 0 <= k < n and 0 <= j < n:
        diagonal02.append(quadrado[j][k])

        j += 1
        k -= 1
    
    somas.append(sum(diagonal02))
    return somas, somas[0]

n = int(input())
quadrado = [list(map(int, input().split())) for _ in range(n)]

somas, k = somar(quadrado)

if checar_igualdade(somas):
    print(k)
else:
    print(0)