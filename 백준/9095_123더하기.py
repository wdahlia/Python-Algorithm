
import sys
sys.stdin = open('9095.txt')

tc = int(input())

dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
for _ in range(tc):
    n = int(input())
    print(dp[n])

