
import sys
sys.stdin = open('1904.txt')

# 0합치는것도 짝수로만 1합치는 것도 짝수로만 밖에 못만든단 소리
# 15746으로 나눈 나머지 출력 - 출력값에 신경쓸것

num = int(input())
N = 10000001
dp = [0] * N

dp[1] = 1
dp[2] = 2

for i in range(3, num + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[num])