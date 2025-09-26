class FenwickTree:
    def __init__(self, N):
        self.n = N
        self.bit = [0] * (self.n + 1)
        self.arr = [0] * (self.n + 1)

    def update(self, i, val):
        delta = val - self.arr[i]
        self.arr[i] = val

        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    
    def prefix_sum(self, i):
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= i & -i
        return result
    
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l-1)
 
N, Q = map(int, input().split())
andares = [0] + list(map(int, input().split()))
eventos = [list(map(int, input().split())) for _ in range(Q)]

ft = FenwickTree(N)

for i in range(1, N+1):
    ft.update(i, andares[i])

for e in eventos:
    if e[0] == 0:
        ft.update(e[1], e[2])
    else:
        print(ft.range_sum(1, e[1]))