def maxmin(matriz):
    maior = matriz[0][0]
    menor = matriz[0][0]

    for a in matriz:
        for b in a:
            if b > maior:
                maior = b
            if b < menor:
                menor = b
    
    return maior, menor

def op1(baldes, i, peso):
    baldes[i-1].append(peso)

def op2(baldes, a, b):
    baldes_limitados = baldes[a-1:b]
    ma, me = maxmin(baldes_limitados)

    for balde in baldes_limitados:
        if (ma in balde and me not in balde) or (ma not in balde and me in balde):
            print(ma-me)
        if ma in balde and me in balde:
            while True:
                

num_baldes, num_operacoes = 10, 5#map(int, input().split())
baldes = [[3], [9], [12], [4], [20], [5], [7], [15], [9], [10]]#[[int(x)] for x in input().split()]
operacoes = [[1, 1, 5], [1, 33, 8], [2, 6, 9], [1, 15, 2], [2, 1, 7]]#[list(map(int, input().split())) for _ in range(num_operacoes)]

for i, j, k in operacoes:
    if i == 1:
        op1(baldes, k, j)
    else:
        print(op2(baldes, j, k))
