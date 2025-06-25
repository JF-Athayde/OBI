def receber_entrada():
    codigos = []
    amigos = []

    num = int(input())

    for i in range(num):
        i1, i2 = input().split()
        codigos.append([i1, int(i2)])
        if i1 != 'T':
            amigos.append(int(i2))

    amigos = list(set(amigos))
    amigos.sort()
    codigos.append([0, 0])

    return codigos, amigos

def corrigir_codigo(codigos):
    codigos_corrigidos = []

    for i in range(1, len(codigos)):
        codigos_corrigidos.append(codigos[i-1])
        if codigos[i][0] != 'T' and codigos[i-1][0] != 'T':
            codigos_corrigidos.append(['T', 1])

    return codigos_corrigidos

def contar_tempo(amigo, codigos_corrigidos):
    tempo = 0
    contar = False # G.O.A.T
    aberto = True # Gambiarra

    for tipo, amigo_c in codigos_corrigidos:
        if amigo_c == amigo and tipo == 'R':
            contar = True
            aberto = True
        if tipo == 'T' and contar:
            tempo += amigo_c # kkkkkkk
        if amigo == amigo_c and tipo == 'E':
            contar = False
            aberto = False
    if aberto:
        return -1
    
    return tempo

codigos, amigos = receber_entrada()

codigos = corrigir_codigo(codigos)

for amigo in amigos:
    tempo = contar_tempo(amigo, codigos)

    print(amigo, tempo)