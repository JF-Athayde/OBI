# Simples Bonita e eficaz
# OBS: Oq eu bati cabeça pra resolver cê n tem noção, já tava pensando em universo multidimencional, grafo

def contar(sequencia):
    frequencia = {num:0 for num in list(set(sequencia))}

    for seq in sequencia:
        frequencia[seq] += 1

    return frequencia

sequencia = list(map(int, input().split()))

if max(contar(sequencia).values()) > (len(sequencia)+1) // 2:
    print('N')
else:
    print('S')