s = input()
dp = [0] * 26

for char in s:
    idx = ord(char) - ord('A')

    melhor_anterior = max(dp[:idx + 1])
    dp[idx] = melhor_anterior + 1

print(max(dp))