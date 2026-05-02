MOD = 10**9 + 7

def add(vector, x, k):
  vector.append(x)

  if len(vector) > k:
     vector.remove(vector[0])
  
def f(n, k, vector):
    if n < k:
      add(vector, 2**n, k)
    elif n == k:
      add(vector, 2**n-1, k)

    else:
      add(vector, sum(vector), k)

    return vector[-1]

n, k = map(int, input().split())

v = []
for i in range(1,n+1):
  f(i, k, v)

print(v[-1] % MOD)
