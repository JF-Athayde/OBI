class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [(0, float('inf'))] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = (arr[l], arr[l])
        else:
            mid = (l + r) // 2
            self.build(arr, 2 * node + 1, l, mid)
            self.build(arr, 2 * node + 2, mid + 1, r)
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def merge(self, left, right):
        return (max(left[0], right[0]), min(left[1], right[1]))

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return (float('-inf'), float('inf'))
        if ql <= l and r <= qr:
            return self.tree[node]
        
        mid = (l + r) // 2
        left = self.query(2 * node + 1, l, mid, ql, qr)
        right = self.query(2 * node + 2, mid + 1, r, ql, qr)
        return self.merge(left, right)

    def update(self, node, l, r, index, value):
        if l == r:
            self.tree[node] = (value, value)
        else:
            mid = (l + r) // 2
            if index <= mid:
                self.update(2 * node + 1, l, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, r, index, value)
            # Atualiza o nó atual após a atualização dos filhos
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

def main():
    baldes = [1, 3, 5, 7, 9]
    seg_tree = SegmentTree(baldes)

    acoes = [('1', 10, 2), ('2', 1, 5), ('2', 2, 4), ('1', 0, 3), ('2', 1, 3)]

    for partes in acoes:
        if partes[0] == '1':
            p, i = partes[1], partes[2] - 1
            seg_tree.update(0, 0, len(baldes) - 1, i, p)
        else:
            a, b = partes[1] - 1, partes[2] - 1
            max_value, min_value = seg_tree.query(0, 0, len(baldes) - 1, a, b)
            print(f"Resultado: {max_value - min_value}")
main()
