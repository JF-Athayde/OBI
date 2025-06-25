def contar_retangulos(k, numeros):
    somas = [0]
    total_retangulos = 0

    for numero in numeros:
        nova_soma = somas[-1] + numero
        somas.append(nova_soma)

        for soma_anterior in somas[:-1]:
            if nova_soma - soma_anterior == k:
                total_retangulos += 1

    return total_retangulos

n, k = map(int, input().split())
numeros = list(map(int, input().split()))

print(contar_retangulos(k, numeros))
