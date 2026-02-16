def prefix_sum(vector):
    ps = [0] * len(vector)
    ps[0] = vector[0]
    for i in range(1, len(vector)):
        ps[i] = ps[i-1] + vector[i]
    return ps


def ps_sum(a, b, ps):
    if a == 0:
        return ps[b]
    return ps[b] - ps[a - 1]


N, F = input().split()
N = int(N)
F = float(F)

areas = list(map(int, input().split()))
areas = areas * 2

ps = prefix_sum(areas)

dp = [[0] * (2*N) for _ in range(2*N)]

for w in range(1, N):
    for a in range(0, 2*N - w):
        b = a + w

        if w == 1:
            dp[a][b] = max(areas[a], areas[b]) * F
        else:
            melhor = float('inf')

            for k in range(a, b):
                esquerda = dp[a][k]
                direita = dp[k+1][b]

                soma_esq = ps_sum(a, k, ps)
                soma_dir = ps_sum(k+1, b, ps)

                custo = esquerda + direita + max(soma_esq, soma_dir) * F

                melhor = min(melhor, custo)

            dp[a][b] = melhor

resposta = float('inf')

for inicio in range(N):
    fim = inicio + N - 1
    resposta = min(resposta, dp[inicio][fim])

print(f"{resposta:.2f}")
