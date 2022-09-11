
import sys
sys.stdin = open('1546.txt')

# 최대값 - m / 모든 점수를 점수/m * 100 으로 고침

N = int(input())
score = list(map(int, input().split()))
M = max(score)
result = 0
for i in range(N):
    result += score[i]/M * 100

print(result/N)
