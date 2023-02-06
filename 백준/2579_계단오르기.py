
import sys
sys.stdin = open('2579.txt')

# dp의 규칙
N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

if N <= 2:
    print(sum(stairs))

else:
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for i in range(3, N+1):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

    print(dp[N])