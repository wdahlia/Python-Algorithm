
import sys
sys.stdin = open('12865.txt')

# 무게 W와 가치 V를 가짐 
# 최대 K 만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있음

N, limit = map(int, input().split())

dp = [[0] * (limit + 1) for _ in range(N+1)]

w = [0]
v = [0]
for _ in range(N):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

for i in range(1, N+1):
    for j in range(1, limit+1):
        if j >= w[i]: # limit무게가 각 물품의 무게보다 작거나 같다 즉, 가방에 넣을 수 있다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][limit])