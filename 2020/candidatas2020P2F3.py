def contar_sequencia(sequencia, a, b):
    cont = 0
    for j in range(a - 1, b):
        gcd_ = 0
        for k in range(j, b):
            gcd_ = gcd(gcd_, sequencia[k])
            if gcd_ == 1:
                break
            else:
                cont += 1
    return cont

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class SegmentTree:
    def __init__(self, data, func, default):
        self.N = len(data)
        self.func = func
        self.default = default

        self.size = 1
        while self.size < self.N:
            self.size *= 2

        self.tree = [default] * (2 * self.size)

        for i in range(self.N):
            self.tree[self.size + i] = data[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        pos = index + self.size
        self.tree[pos] = value

        while pos > 1:
            pos //= 2
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, l, r):
        res_left = self.default
        res_right = self.default
        l += self.size
        r += self.size

        while l < r:
            if l % 2 == 1:
                res_left = self.func(res_left, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res_right = self.func(self.tree[r], res_right)
            l //= 2
            r //= 2

        return self.func(res_left, res_right)
    
    def sequencia(self):
        return self.tree[self.size : self.size + self.N]


N, M = map(int, input().split())
S = list(map(int, input().split()))
O = [list(map(int, input().split())) for _ in range(M)]

st = SegmentTree(S, gcd, 0)
cont = 0

for o in O:
    x, y, z = o
    if x == 1:
        st.update(y - 1, z)
    elif x == 2:
        print(contar_sequencia(st.sequencia(), y, z))
