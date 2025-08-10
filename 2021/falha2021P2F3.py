n = int(input())
passwords = [str(input()) for _ in range(n)]

cont = 0
passwords.sort(key=len)

for i in range(n):
    a = passwords[i]
    for j in range(i+1, n):
        b = passwords[j]
        if i == j:
            continue

        if a in b:
            cont += 1
        if b in a:
            cont += 1

print(cont)