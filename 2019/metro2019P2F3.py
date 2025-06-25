def bfs(start, grafo):
    queue = [start]
    visitados = {start: 0}
    recorde = 0
    no_final = start
    
    while len(queue) > 0:
        no_atual = queue.pop(0)
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados[vizinho] = visitados[no_atual] + 1
                queue.append(vizinho)
                if visitados[vizinho] > recorde:
                    recorde = visitados[vizinho]
                    no_final = vizinho
    return no_final, recorde, visitados

def encontrar_diametro(grafo):
    no_distante01, _, _ = bfs(list(grafo.keys())[0], grafo)
    no_distante02, diametro, distancia = bfs(no_distante01, grafo)

    caminho = []
    while no_distante02 != no_distante01:
        caminho.append(no_distante02)
        no_distante02 = min(grafo[no_distante02], key=lambda x: distancia[x])  # Pegamos o pai mais próximo de u
    caminho.append(no_distante01)

    return caminho

def encontrar_centro(caminho):
    if len(caminho) % 2 == 1:
        return caminho[len(caminho)//2]
    else:
        return caminho[len(caminho) //2-1]

def receber_entrada():
    N, M = map(int, input().split())

    grafo_02 = {}
    grafo_01 = {}

    for i in range(1, N + 1):
        grafo_02[i] = []
    for i in range(1, M + 1):
        grafo_01[i] = []

    for _ in range(N - 1):
        A, B = map(int, input().split())
        grafo_02[A].append(B)
        grafo_02[B].append(A)

    for _ in range(M - 1):
        X, Y = map(int, input().split())
        grafo_01[X].append(Y)
        grafo_01[Y].append(X)

    return grafo_02, grafo_01

adj_circulo, adj_quadrado = receber_entrada()

print(encontrar_centro(encontrar_diametro(adj_circulo)), 
      encontrar_centro(encontrar_diametro(adj_quadrado)))
