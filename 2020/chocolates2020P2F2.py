def promocao(precos):
    if len(precos) == 3:
        precos.sort(reverse=True)
        return precos[0] + precos[1]
    return sum(precos)

def definir_grupos(precos):
    precos.sort(reverse=True)
    
    pote = 0

    for i in range(0, len(precos), 3):
        grupo = precos[i:i+3]
        pote += promocao(grupo)
    
    return pote

precos = [int(input()) for _ in range(int(input()))]
print(definir_grupos(precos))
