def dinamica(n, mod):
    if n == 2:
        return 5
    if n == 1:
        return 1
    
    if n == 0:
        return 1
    
    vetor_dinamico = [0] * (n+1)
    vetor_dinamico[0] = 1
    vetor_dinamico[1] = 1
    vetor_dinamico[2] = 5

    for i in range(3, n+1):
        vetor_dinamico[i] = (vetor_dinamico[i-1] + 4*vetor_dinamico[i-2] + 2*vetor_dinamico[i-3]) % mod
    
    return vetor_dinamico[-1]

print(dinamica(int(input()), 10**9+7))