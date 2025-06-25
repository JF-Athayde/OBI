#Crifra da Nlongônia
def first_min(lista):
    m = min(lista)
    for c, item in enumerate(lista):
        if item == m:
            return c

def distancias(c, lista02):
    return [abs(a-b) for a, b in zip([c for _ in range(len(lista02))], lista02)]
        
def proxima_vogal(letra, alphabeto, vogais):
    i_letra = alphabeto.index(letra)
    i_vogais = [alphabeto.index(d) for d in vogais]

    distancias_ = distancias(i_letra, i_vogais)
    return vogais[first_min(distancias_)]

palavra = list(input())
alphabeto = list('abcdefghijklmnopqrstuvxzz')
vogais = list('aeiou')

for letra in palavra:
    print(letra, end='')
    if letra not in vogais and letra != ' ':
        print(proxima_vogal(letra, alphabeto, vogais), end='')
        cont = 1
        while True:
            proxima_consoante = alphabeto[alphabeto.index(letra)+cont]
            if proxima_consoante not in vogais:
                print(proxima_consoante, end='')
                break
            cont += 1
