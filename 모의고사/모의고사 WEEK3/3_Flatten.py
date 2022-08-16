import sys

sys.stdin = open("_Flatten.txt")

import heapq 

# 평탄화 작업 
# 10개의 테스트 케이스
# 덤프 횟수 - 제한되어 있음
# 상자의 높이 값 주어짐
# heapq를 사용해볼까

T = 10

for i in range(1, T+1):
    dump_n = int(input())
    box_h = list(map(int, input().split()))

    heapq = sorted(box_h)


    while dump_n != 0:
        cnt = 0
        for i in range(100):
            if box_h[i] != max_box:
                box_h[i] += 1
                cnt += 1
            else:
                box_h[i] -= cnt

        print(box)
            

