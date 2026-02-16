n = int(input())
postes = list(map(int, input().split()))

consertados = 0
substituidos = 0

for p in postes:
    if 50 <= p < 85:
        consertados += 1
    if p < 50:
        substituidos += 1

print(substituidos, consertados)