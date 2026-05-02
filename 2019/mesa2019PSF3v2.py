A = int(input())
B = int(input())

ana = A%3
bia = B%3

if bia == ana:
    bia += 1

if bia == 3:
    bia = 0

cadeiras = [0, 0, 0]

cadeiras[ana] = 1
cadeiras[bia] = 1

for cont, c in enumerate(cadeiras):
    if c == 0:
        print(cont)
        break
