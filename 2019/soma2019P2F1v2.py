n, alvo = map(int, input().split())  # usar outro nome para evitar conflito com 'k'
sequencia = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
cont = 0

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + sequencia[i]

for i in range(n):
    for j in range(i + 1, n + 1):
        if prefix_sum[j] - prefix_sum[i] == alvo:
            cont += 1

print(cont)
