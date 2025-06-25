letras = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
codigos = list(map(str, [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]))

alphanumerico = input()
resposta = []

for i in alphanumerico:
    if i in letras:
        resposta.append(codigos[letras.index(i)])
    else:
        resposta.append(i)

print(''.join(resposta))