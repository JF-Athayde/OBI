def desocupado(mesa):
    if mesa == [0, 1]:
        return 2
    if mesa == [1, 2]:
        return 0
    else:
        return 1

A = int(input())
B = int(input())

cA = A%3
cB = B%3

if cA == cB:
    if cB != 3:
        cB += 1
    else:
        cB == 0

print(desocupado(sorted([cA, cB])))
