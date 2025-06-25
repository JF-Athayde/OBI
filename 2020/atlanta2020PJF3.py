def retangulizar(azul, branco):
    A = azul+branco

    for l in range(1, A): # Azul = 2L + 2C - 4
        if A % l == 0:
            c = int(A/l)
            if 2*l + 2*c - 4 == azul and l*c-2*l-2*c+4 == branco:
                return min(c, l), max(l, c)

    return -1, -1

azul = int(input())
branco = int(input())

x, y = retangulizar(azul, branco)
print(x, y)