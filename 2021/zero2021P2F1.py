n = int(input())
num = [int(input()) for _ in range(n)]

num = num[::-1]
resposta = []
ignorar = 0

for i in num:
    if i == 0:
        ignorar += 1
    else:
        if ignorar > 0:
            ignorar -=1
        else:
            resposta.append(i)

print(sum(resposta))