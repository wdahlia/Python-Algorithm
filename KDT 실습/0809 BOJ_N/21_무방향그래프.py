
from pprint import pprint
import sys
sys.stdin = open('21.txt')

N, M = map(int, input().split())

# 행렬
matrix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

pprint(matrix)

# 리스트 
arr = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

print(arr)
