def juntar(x, somas):
    somas.sort(reverse=True)
    if x < somas[0]:
        somas[0] = x

def somar_etiquetas(fita, N, K, C):
    menores_somas = [float('inf')] * K

    for i in range(N-C+1):
        trecho = fita[i:i+C]
        soma = sum(trecho)

        juntar(soma, menores_somas)

    return sum(menores_somas)

N, K, C = 12, 2, 3 #map(int, input().split())
fita = list(map(int, '1 22 4 -8 9 2 10 -1 5 5 32 -11'.split())) #list(map(int, input().split()))

sobrepostas = somar_etiquetas(fita, N, K, C)
soma_total = sum(fita)

print(soma_total-sobrepostas)

