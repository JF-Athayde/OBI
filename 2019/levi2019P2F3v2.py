class Fenwick:
    def __init__(self,n):
        self.n = n
        self.bit = [0]*(n+1)

    def update(self,i,v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self,i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

N, P, Q = map(int, input().split())
coordenadas = [tuple(map(int, input().split())) for _ in range(N)]
coordenadas.sort()

V = [Q*y - P*x for x, y in coordenadas]

vals = sorted(set(V))

comp = {}
for i,v in enumerate(vals):
    comp[v] = i+1

fw = Fenwick(len(vals))

ans = 0
for v in V:
    idx = comp[v]
    menores_ou_iguais = fw.query(idx)
    ans += menores_ou_iguais
    fw.update(idx,1)

print(ans)