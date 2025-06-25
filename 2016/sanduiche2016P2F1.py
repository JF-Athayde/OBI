def contagem_sequencial(vetor, alvo):
    cont = 0

    n = len(vetor)
    for i in range(n):
        for f in range(i+1, n+1):
            v = sum(vetor[i:f])
            if v == alvo:
                cont += 1
    return cont

def soma_progressiva(vetor):
    vetor_soma = []
    pote = 0

    for i in vetor:
        pote += i
        vetor_soma.append(pote)

    return vetor_soma

def soma_regressiva(vetor):
    r = soma_progressiva(vetor[::-1])
    return r

def borda(vetor, alvo):
    pre = soma_progressiva(vetor)
    pos = soma_regressiva(vetor)[::-1]

    cont = 0

    for ai in range(len(pre)):
        for bi in range(len(pos)):
            if ai < bi and pre[ai] + pos[bi] == alvo:
                cont += 1
    return cont

def main(D, sanduiche):
    return contagem_sequencial(sanduiche, D) + borda(sanduiche, D)

N, D = map(int, input().split())
sanduiche = list(map(int, input().split()))

print(main(D, sanduiche))
