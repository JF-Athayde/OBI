def minimo_dias_para_moedas(n, f, ciclos):
    esquerda = 1
    direita = 10**8
    resposta = direita

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        moedas = sum(meio // c for c in ciclos)

        if moedas >= f:
            resposta = meio
            direita = meio - 1
        else:
            esquerda = meio + 1

    return resposta

n, f = map(int, input().split())
ciclos = list(map(int, input().split()))

print(minimo_dias_para_moedas(n, f, ciclos))
