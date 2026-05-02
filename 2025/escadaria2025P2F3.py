n = 5
escada = [4, -1, -1, -1, 2]

a = 0
b = 4

for i, degrau in enumerate(escada):
    if degrau == -1:
        distancia = b-i
        diferencia = escada[b]-escada[i-1]

        print(distancia, diferencia)
        input(':>')