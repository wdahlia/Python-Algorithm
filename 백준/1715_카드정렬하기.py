
import sys
sys.stdin = open('1715.txt')

import heapq
# 최소한의 비교
# 정렬해야될듯?

N = int(input())

heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0
for _ in range(N-1):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sumNum = num1 + num2
    heapq.heappush(heap, sumNum)
    result += sumNum

print(result)
