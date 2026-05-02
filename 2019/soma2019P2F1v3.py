def solve(seq, N, K):
    soma = 0
    cont = 0
    freq = {0: 1}

    for x in seq:
        soma += x

        if soma - K in freq:
            cont += freq[soma - K]

        if soma in freq:
            freq[soma] += 1
        else:
            freq[soma] = 1

    return cont


N, K = map(int, input().split())
seq = list(map(int, input().split()))

print(solve(seq, N, K))