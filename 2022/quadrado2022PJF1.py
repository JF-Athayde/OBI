n = int(input())

matriz = [list(map(int, input().split())) for _ in range(n)]

x = -1
y = -1
value = -1

for j, linha in enumerate(matriz):
    for k, item in enumerate(linha):
        if item == 0:
            x = j+1
            y = k+1

            for i in range(n):
                if i != j:
                    value = sum(matriz[i]) - sum(matriz[j])
                    break
            break

print(value)
print(x)
print(y)