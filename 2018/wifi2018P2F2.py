def interiors(a, b):
    return a.x1 > b.x1 and a.x2 < b.x2 and a.y1 < b.y1 and a.y2 > b.y2

class Room:
    def __init__(self, x1, y1, x2, y2, area, i):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = area
        self.i = i

class Tree:
    def __init__(self):
        self.tree = []
        self.parents = []
        self.children_count = []
    
    def build(self, N):
        self.parents = [-1] * N
        self.children_count = [0] * N

        for i in range(N):
            x1, y1, x2, y2 = map(int, input().split())
            area = (x2 - x1) * (y1 - y2)
            
            self.tree.append(Room(x1, y1, x2, y2, area, i))
        
        self.tree.sort(key=lambda room: room.area, reverse=True)
    
        for j in range(1, N):
            for k in range(j-1, -1, -1):
                if interiors(self.tree[j], self.tree[k]):
                    self.parents[self.tree[j].i] = self.tree[k].i
                    self.children_count[self.tree[k].i] += 1
                    break


N = int(input())
obj = Tree()
obj.build(N)
obj.fill(N)

root = obj.parents.index(-1)
print(obj.children_count[root])
