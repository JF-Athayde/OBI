def busca_binaria(lista, cond):
    ini, fim = 0, len(lista)
    while ini < fim:
        meio = (ini + fim) // 2
        if cond(lista[meio]):
            fim = meio
        else:
            ini = meio + 1
    return ini

lista = ["Oi", "OBI", "Python", "Nlogônia", "Competição"]
lista.sort(key=len)
x = 5

i = busca_binaria(lista, lambda s: len(s) > x)
print("Índice encontrado:", i)
print("Strings filtradas:", lista[i:])
