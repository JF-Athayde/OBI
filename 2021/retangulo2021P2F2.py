def definir_posicoes(vetor):
    a = []
    pote = vetor[0]

    for v in vetor:
        a.append(pote)
        pote += v

    return a

n = 8 #int(input())
distancias = [3, 3, 4, 2, 6, 2, 2, 2] #list(map(int, input().split()))
posicoes = definir_posicoes(distancias) # Partindo do distancias[0]
print(posicoes)