def fatorar(n):
    fatores = []
    
    while n % 2 == 0:
        fatores.append(2)
        n //= 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            fatores.append(i)
            n //= i
        i += 2
    
    if n > 1:
        fatores.append(n)
    
    return fatores

def diminuir_K(K):
    fatores = []

    for b in K:
        fatores += list(set(fatorar(b)))

    return list(set(fatores))

def quase_primo(K, N):
    proibidos = [False] * (N+1)

    for k in diminuir_K(K):
        for m in range(k, N+1, k):
            proibidos[m] = True

    cont = 0
    for i in range(1, N+1):
        if not proibidos[i]:
            cont += 1
    
    return cont

N, _ = map(int, input().split())
K = list(map(int, input().split()))

print(quase_primo(K, N))