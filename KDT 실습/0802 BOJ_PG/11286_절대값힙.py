
import sys
sys.stdin = open('11286.txt')

# import sys
# input = sys.stdin.readline

import heapq


T = int(input())

heap = []
for _ in range(T):
    x = int(input())
    
    if x != 0:
        # heapq.heappush(heap, (abs(x), x))
        if x < 0:
            heapq.heappush(heap, (-x, x))
        else:
            heapq.heappush(heap, (x, x))
    else:
        if len(heap) == 0:                  # len(heap)으로 표현해도 무방
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result[1])
