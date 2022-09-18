
import sys
sys.stdin = open('11047.txt')

# N종류의 동전을 가지고 있다
# 그 가치의 합을 K로 만들려고한다
# 필요한 동전 개수의 최솟값을 구하는 것

N, K = map(int, input().split())

values = []
for _ in range(N):
    coin = int(input())
    values.append(coin)

values.sort(reverse=True)

result = 0
for value in values:
    if K < value:
        continue
    else:
        if K % value == 0:
            result += K // value
            break
        else:
            result += K // value
            K -= (K // value) * value 
print(result)
