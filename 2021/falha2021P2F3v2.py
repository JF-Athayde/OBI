def busca_binaria(lista, cond):
    ini, fim = 0, len(lista)
    while ini < fim:
        meio = (ini + fim) // 2
        if cond(lista[meio]):
            fim = meio
        else:
            ini = meio + 1
    return ini

def limitar_possibilidades(senha, senhas):
    x = len(senha)
    i = busca_binaria(senhas, lambda s: len(s) >= x)

    return senhas[i:]

def checar_senha(senhas, senha):
    possibilidades = limitar_possibilidades(senha, senhas)
    cont = 0

    for a in possibilidades:
        if senha in a:
            cont += 1
    
    return cont-1

N = int(input())
Senhas = [input() for _ in range(N)]
Senhas.sort(key=len)

cont = 0
for senha in Senhas:
    cont += checar_senha(Senhas, senha)

print(cont)