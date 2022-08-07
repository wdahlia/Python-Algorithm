import sys
sys.stdin = open('2750_수정렬하기.txt')

import heapq

T = int(input())

heap = []
for _ in range(T):
    n = int(input())

    heapq.heappush(heap, n)

for _ in range(T):
    result = heapq.heappop(heap)
    print(result)
