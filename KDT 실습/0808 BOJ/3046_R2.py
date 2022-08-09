
# R1, S 입력받아 R2 출력
# S = (R1+R2)/2 평균

# 11 15 ; 19

# 수학으로 생각해서 풀면되는 간단한 문제

import sys
sys.stdin = open('3046.txt')

R1, S = list(map(int, input().split()))

R2 = 2 * S - R1

print(R2)
