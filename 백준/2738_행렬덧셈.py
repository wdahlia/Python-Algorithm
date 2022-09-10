
import sys
sys.stdin = open('2738.txt')

# N개의 줄 행렬 A 원소 M개 차례로 주어짐
# N개의 줄 행렬 B 원소 M개 차례로 주어짐
# 정수이다 즉 안의 값이 - 인 경우 존재

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(2*N)]

for i in range(N):
    result = []
    for j in range(M):
        result.append(matrix[i][j] + matrix[i+N][j])
    print(*result)
    