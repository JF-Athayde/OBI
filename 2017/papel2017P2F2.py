def f(lista):
    resultado = [lista[0]]
    for i in range(1, len(lista)):
        if lista[i] - 1 != lista[i - 1]:
            resultado.append(lista[i])
    return resultado

def definir_corte(alturas):
    max_pecas = 0
    cortes = set(alturas)
    
    for crt in cortes:
        a = [i for i, alt in enumerate(alturas) if alt > crt] 
        
        if len(a) > 0:
            max_pecas = max(max_pecas, len(f(a)) + 1)

    return max_pecas

n = int(input())
alturas = list(map(int, input().split()))

print(definir_corte(alturas))
