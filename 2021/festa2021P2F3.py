def lista(N):
    if N >= 10000:
        return [a+1 for a in range(10000)]
    else:
        return [a+1 for a in range(N)]

N = 10
M = 2
T = [2, 3]

Lista = lista(N=N)

for Ti in T:
    nova_lista = []
    for Ni in range(len(Lista)):
        if (Ni + 1) % Ti != 0:
            nova_lista.append(Lista[Ni])
        
        if len(nova_lista) >= 10000:
            break
    Lista = nova_lista.copy()

for i in Lista[:10000]:
    print(i)