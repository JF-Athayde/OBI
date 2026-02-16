def mostrar(num):
    num_str = str(num)
    for n in num_str:
        print(n, end=' ')
    print()

def numerizar(lista):
    a = [str(n) for n in lista]
    return int(''.join(a))

def desmatrizar(matriz):
    nova_matriz = []
    for lista in matriz:
        nova_matriz.append(numerizar(lista))
    return nova_matriz
    
input()
S = list(map(int, input().split()))
#S = list(map(int, '7 3 0 1 0 5 6 9 7 5 4 2'.split()))

cincos = []
zeros = []

for i, s in enumerate(S):
    if s == 5:
        cincos.append(i)
    if s == 0:
        zeros.append(i)

sequencias = []
last = S[-1]

for c in cincos:
    S_ = S.copy()
    S_[-1] = 5
    S_[c] = last
    sequencias.append(S_)

for z in zeros:
    S_ = S.copy()
    S_[-1] = 0
    S_[z] = last
    sequencias.append(S_)

seqs = desmatrizar(sequencias)

if len(seqs) == 0:
    print(-1)
else:
    mostrar(max(desmatrizar(sequencias)))
