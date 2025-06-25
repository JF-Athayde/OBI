def preencher_pretas(L, C, pretas):
    tabuleiro = [[0 for _ in range(C)] for _ in range(L)]

    for x, y in pretas:
        tabuleiro[x-1][y-1] = 1
    return tabuleiro

def preencher_brancas(L, C, matriz):
    brancos = 0

    for j in range(L):
        for k in range(C):
            if matriz[j][k] == 0:
                # Vazio
                vizinho_preto = False
                vizinho_branco = False

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nj = dx+j
                    nk = dy+k

                    if 0 <= nj < L and 0 <= nk < C:
                        if matriz[nj][nk] == 1:
                            vizinho_preto = True
                        if matriz[nj][nk] == 2:
                            vizinho_branco = True
                if vizinho_preto and not vizinho_branco:
                    matriz[j][k] = 2
                    brancos += 1
    return brancos

l, c = map(int, input().split())
p = int(input())
posicoes_pretas = [tuple(map(int, input().split())) for _ in range(p)]

tabuleiro = preencher_pretas(l, c, posicoes_pretas)
brancos = preencher_brancas(l, c, tabuleiro)

print(brancos)
