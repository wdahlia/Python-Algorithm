
import sys
sys.stdin = open('11659.txt')

# 수의 개수 n, 합을 구해야하는 횟수 m이 주어
# m개의 줄에는 합을 구해야하는 i,j가 주어짐

input = sys.stdin.readline

N, M = map(int, input().split())

nList = list(map(int, input().split()))
sumList = [0] * (N+1)

num = 0
for i in range(N):
    num += nList[i]
    sumList[i+1] = num

for _ in range(M):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i-1])
    