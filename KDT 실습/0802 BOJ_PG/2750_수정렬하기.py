
import sys
sys.stdin = open('2750.txt')

import heapq

T = int(input())

heap = []
for _ in range(T):
    n = int(input())

    heapq.heappush(heap, n)

for _ in range(T):
    result = heapq.heappop(heap)
    print(result)
