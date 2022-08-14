
import sys
sys.stdin = open('14720.txt')

# 딸기우유 0 > 초코우유 1 > 바나나우유 2

N = int(input())

stores = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if stores[i] == cnt % 3:
        cnt += 1

print(cnt)
