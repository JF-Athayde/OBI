import heapq

def indeciso(heap, decisos):
    while heap:
        preco, tipo = heap[0]
        if decisos[tipo] and decisos[tipo][0] == preco:
            return tipo, preco
        heapq.heappop(heap)
    return (float('inf'), float('inf'))


N, T = map(int, input().split())
tipos = list(map(int, input().split()))
precos = list(map(int, input().split()))

C = int(input())
operacoes = list(map(int, input().split()))

decisos = {tipo: [] for tipo in range(T + 1)}

for p, t in zip(precos, tipos):
    decisos[t].append(p)

for prod in decisos:
    decisos[prod].sort()

heap = []
for t in decisos:
    if decisos[t]:
        heapq.heappush(heap, (decisos[t][0], t))

total = 0

for op in operacoes:
    if op == 0:
        tipo, preco = indeciso(heap, decisos)
        if preco == float('inf'):
            continue

        total += preco
        decisos[tipo].pop(0)

        if decisos[tipo]:
            heapq.heappush(heap, (decisos[tipo][0], tipo))

    else:
        if decisos[op]:
            preco = decisos[op][0]
            total += preco
            decisos[op].pop(0)

            if decisos[op]:
                heapq.heappush(heap, (decisos[op][0], op))

print(total)