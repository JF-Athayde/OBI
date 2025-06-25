botas = [list(input().split()) for _ in range(int(input()))]
bostas = {a: b for a, b in botas}
print(bostas)

#Checagem em pares O(n²)
cont = 0

for a in range(len(botas)):
    for b in range(len(botas)):
        if a != b:
            if botas[a] == botas[b]:
                cont += 1
print(cont)