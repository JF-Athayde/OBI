class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        # build inicial
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    # Atualiza a posição i (0-based) para o valor val
    def update(self, i, val):
        pos = i + self.size
        self.tree[pos] = val
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos //= 2

    # Consulta a soma do intervalo [l, r) (0-based, r exclusivo)
    def query(self, l, r):
        res = 0
        l += self.size
        r += self.size
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


# Exemplo de uso:

a = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
st = SegmentTree(a)

# soma do intervalo [1, 5) → índices 1 até 4
print(st.query(1, 5))  # 2+1+5+4 = 12

# atualiza posição 2 para valor 7 (antes era 1)
st.update(2, 7)

# soma novamente intervalo [1, 5)
print(st.query(1, 5))  # 2+7+5+4 = 18
