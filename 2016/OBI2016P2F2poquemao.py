N = int(input())
X = int(input())
Y = int(input())
Z = int(input())

pokemons = [X, Y, Z]
pokemons.sort()

cont = 0
for p in pokemons:
    if N >= p:
        N -= p
        cont += 1

print(cont)