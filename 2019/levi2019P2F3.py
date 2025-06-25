class FenwickTree: # Ou algoritimo BIT
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

def count_pairs(coordinate, P, Q):
    N = len(coordinate)

    points = []
    for x, y in coordinate:
        S = Q * y - P * x
        points.append((x, S))
    points.sort()

    Sv = [s for _, s in points]
    Sv_sort = sorted(set(Sv))
    compress = {v: id+1 for id, v in enumerate(Sv_sort)}

    fenwick = FenwickTree(len(Sv_sort))
    count = 0

    for x, s in points:
        id_s = compress[s]
        count += fenwick.query(id_s)

        fenwick.update(id_s, 1)
    return count

def solve():
    N, P, Q = map(int, input().split())
    titans = [tuple(map(int, input().split())) for _ in range(N)]

    result = count_pairs(titans, P, Q)
    print(result)

solve()