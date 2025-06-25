MOD = 10**9 + 7

def main(N, K):
  dp = [[0] * K for _ in range(N+1)]
  dp[0][0] = 1

  for i in range(1, N+1):
    dp[i][0] = sum(dp[i - 1])

    for j in range(1, K):
      dp[i][j] = dp[i - 1][j - 1]
  
  return sum(dp[N]) % MOD

N, K = map(int, input().split())

print(main(N, K))