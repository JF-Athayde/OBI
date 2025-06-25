n = int(input())
postes = list(map(int, input().split()))

substituidos = 0
consertados = 0

for poste in postes:
    if 50 <= poste < 85:
        consertados += 1
    if poste < 50:
        substituidos += 1

print(substituidos, consertados) 