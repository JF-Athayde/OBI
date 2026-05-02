class SegmentTree:
    def __init__(self, data, n):
        self.n = n
        self.tree = [[0, 0, 0, 0, 0] for _ in range(2 * self.n)]
        
        # folhas
        for i in range(len(data)):
            ma = max(data[i])
            mi = min(data[i])
            print([mi, i, ma, i, 0])
            self.tree[self.n + i] = [mi, i, ma, i, 0]

        # construir
        for i in range(self.n - 1, 0, -1):
            a = self.tree[2 * i]
            b = self.tree[2 * i + 1]
            
            min_a = (a[0], a[1])
            min_b = (b[0], b[1])

            max_a = (a[2], a[3])
            max_b = (b[2], b[3])
            
            min_s = min([(a[2], a[3]), (b[2], b[3])])
            max_s = max([(a[2], a[3]), (b[2], b[3])])

            r = abs(max_b[0] - min_a[0])
            r_ = abs(max_a[0] - min_b[0])
            
            if r < r_:
                r = r_

            print([min_s[0], min_s[1], max_s[0], max_s[1], r])

            self.tree[i] = [min_s[0], min_s[1], max_s[0], max_s[1], r]
                
        input(':>')

    def add(self, idx, value):
        pos = idx + self.n
        total = self.tree[pos]+value
        self.tree[pos] = [min(total), max(total)]

        while pos > 1:
            pos //= 2
            a = self.tree[2 * pos]
            b = self.tree[2 * pos + 1]

            c = [min(a), max(b)]
            d = [max(a), min(b)]

            if abs(c[0]-c[1]) > abs(d[0]-d[1]):
                self.tree[pos] = c
            else:
                self.tree[pos] = d

    def query(self, l, r):
        if l > r:
            l, r = r, l  # corrige automaticamente

        l += self.n
        r += self.n

        res = [float('inf'), float('-inf')]

        while l <= r:
            if l % 2 == 1:
                res[0] = min(res[0], self.tree[l][0])
                res[1] = max(res[1], self.tree[l][1])
                l += 1

            if r % 2 == 0:
                res[0] = min(res[0], self.tree[r][0])
                res[1] = max(res[1], self.tree[r][1])
                r -= 1

            l //= 2
            r //= 2

        return res

    def t(self):
        l = []
        for i in range(self.n):
            l.append(self.query(i, i))
        return l

N, M = 10, 5#map(int, input().split())
baldes = [[3], [10, 4], [6, 2, 15], [8, 9], [7], [9, 9, 101]]#[[i] for i in list(map(int, input().split()))]
ops = [[1, 1, 5], [1, 33, 8], [2, 6, 9], [1, 15, 2], [2, 1, 7]]#[list(map(int, input().split())) for _ in range(M)]

st = SegmentTree(baldes, N)

for op in ops:
    if op[0] == 1:
        st.add(op[2]-1, [op[1]])
    else:
        if op[1] == op[2]:
            print(0)
        else:
            a, b = st.query(op[2]-1, op[1]-1)
            print(b-a)
