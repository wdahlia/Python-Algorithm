
import sys
sys.stdin = open('9455.txt')

from pprint import pprint

T = int(input())

for _ in range(T):
    n, m = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    sum_cnt = 0
    for col in range(m):
        cnt = 0
        for row in range(n):
            if matrix[row][col] == 1:
                cnt += 1
            else:
                sum_cnt += cnt
    
    print(sum_cnt)
