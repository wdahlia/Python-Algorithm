
# 유방향 그래프 인접 행렬, 인접 리스트 표현
# 정점의 개수 N, 간선의 개수 M
# 시작점 u와 끝점 v

from platform import architecture
from pprint import pprint 
import sys
sys.stdin = open('22.txt')

N, M = map(int, input().split())

# 행렬로 표현
matrix = [[0] * (N+1) for _ in range(N+1)]
# N+1의 이유는 코딩에서는 인덱스가 0으로 시작하지만
# 지금 주어진 시작점은 1부터 시작하기 때문

for _ in range(M):
    start, end = map(int, input().split())
    matrix[start][end] = 1

pprint(matrix)

# 리스트로 표현
arr = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)

print(arr)
