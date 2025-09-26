class SegmentTree:
    def __init__(self, data, func, default):
        self.n = len(data)
        self.func = func
        self.default = default
        self.tree = [default] * (2 * self.n)
        
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        pos = idx + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        res = self.default
        while l <= r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = self.func(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

arr = [5, 3, 7, 6, 2]

st = SegmentTree(arr, func=lambda a, b: a + b, default=0)

print("Soma [0, 2]:", st.query(0, 2))
print("Soma [1, 3]:", st.query(1, 3))
print("Soma [2, 4]:", st.query(2, 4))

st.update(2, 10)

print("Soma [0, 2] após update:", st.query(0, 2))
print("Soma [2, 4] após update:", st.query(2, 4))

st_min = SegmentTree(arr, func=min, default=float("inf"))
print("Mínimo [1, 3]:", st_min.query(1, 3))