def bfs(grafo, N, inicio):
    inicio -= 1
    dist = [-1] * N
    fila = [inicio]
    dist[inicio] = 0
    ini = 0
    cont = 0

    while ini < len(fila):
        no_atual = fila[ini]
        ini += 1

        for vz in grafo[no_atual]:
            if dist[vz] == -1 and alturas[vz] < alturas[no_atual]:
                dist[vz] = dist[no_atual] + 1
                fila.append(vz)
                cont += 1
    
    return cont

S, T, P = map(int, input().split())
alturas = list(map(int, input().split()))
arestas = [list(map(int, input().split())) for _ in range(T)]

grafo = [[] for _ in range(S)]

for a, b in arestas:
    grafo[a-1].append(b-1)
    grafo[b-1].append(a-1)

cont = bfs(grafo, S, P)
print(cont)
