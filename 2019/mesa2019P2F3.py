def encontrar_diferente(a, b, lista):
    return next(c for c in lista if c not in {a, b})

def proximo(n):
    if n == 1:
        return 2
    elif n == 2:
        return 0
    else:
        return 1
    
def last(n):
    i = 1
    for _ in range(n-1):
        i = proximo(i)
    return i

A = int(input())
B = int(input())

ana = last(A)
bea = last(B)

if ana == bea:
    bea = proximo(bea)

print(encontrar_diferente(ana, bea, [1, 2, 0]))