T = int(input())
N = int(input())
X = [int(input()) for _ in range(N)]

X.append(T)
X.sort()

record = float('inf')
for i in range(1, N):
    a = (X[i] - X[i-1])/2 + (X[i+1] - X[i])/2
    if a < record:
        record = a

print(f'{round(record):.2f}')