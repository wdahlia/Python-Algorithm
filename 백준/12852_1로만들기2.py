
n = int(input())
result = [n]

dp = [0] * 1000001

for i in range(2, n + 1):
  dp[i] = dp[i - 1] + 1

  if i % 2 == 0:
    # 2로 나누어 떨어진다면
    dp[i] = min(dp[i], dp[i // 2] + 1)

  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)

num = n
dec = dp[n] - 1
for idx in range(n, 0, -1):
  if dp[idx] == dec:
    if (idx + 1 == num or idx * 2 == num or idx * 3 == num):
      num = idx
      result.append(idx)
      dec -= 1

print(dp[n])
print(*result)
