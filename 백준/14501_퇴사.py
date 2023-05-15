
import sys
sys.stdin = open('14501.txt')

# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50

N = int(input())
table = list(list(map(int, input().split())) for _ in range(N))
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+table[i][0], N+1):
        if dp[j] < dp[i] + table[i][1]:
            dp[j] = dp[i] + table[i][1]

print(dp[-1])

