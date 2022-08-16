
import sys
sys.stdin = open('2693.txt')

import heapq

# N번째 큰 값을 출력하는 프로그램
# 테스트 케이스는 한 줄, 원소 10개가 공백으로 구분되어 주어짐
# 배열 A에서 3번째 큰 값 출력

# sorted해서 3번째로 큰 값 빼내기
T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])

T = int(input())

# 큰 값 구하는 방법, heapq에서 3번째로 pop한 값 출력
for _ in range(T):
    arr = list(map(int, input().split()))
    max_heap = []
    for a in arr:
        heapq.heappush(max_heap, (-a, a))

    i = 0
    while i != 3:
        result = heapq.heappop(max_heap)[1]
        i += 1
    print(result)
        