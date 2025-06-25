def buscar_maior_k(vetor, N):
    vetor.sort(reverse=True)
    for i in range(N):
        if vetor[i] <= i:
            return i
        
N = int(input())
respostagens = [int(input()) for _ in range(N)]

print(buscar_maior_k(respostagens, N))