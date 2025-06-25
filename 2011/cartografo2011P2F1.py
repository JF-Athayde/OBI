def bfs(grafo):
    inicio = 1
    visitados = set()
    fila = [(inicio, 0)]
    maior_distancia = 0

    while fila:
        no_atual, distancia = fila.pop(0)

        if distancia > maior_distancia:
            maior_distancia = distancia
        
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, distancia+1))
    
    return maior_distancia

n = int(input())
grafo = {i: [] for i in range(1, n+1)}

for i in range(1, n):
    a, b = map(int, input().split())

    grafo[a].append(b)
    grafo[b].append(a)

print(bfs(grafo))