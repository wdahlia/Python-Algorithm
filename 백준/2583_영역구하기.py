
import sys
sys.stdin = open('2583.txt')
from pprint import pprint

# 주어진 모눈종이에 직사각형을 그리면 색칠이 되지않은 부분들이 영역으로 나누어지게 됨
# 몇 개의 분리된 영역으로 나누어지는지 분리된 각 영역의 넓이는 얼마인지를 출력

M, N, K = map(int, input().split())
matrix = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(M-y2, M-y1):
        for c in range(x1, x2):
            matrix[r][c] = 1


def dfs(x, y):

    area = 1
    stack = [(x, y)]

    while len(stack):
        row, col = stack.pop()
        for idx in range(4):
            nx = row + dx[idx]
            ny = col + dy[idx]
            if -1 < nx < M and -1 < ny < N:
                if matrix[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    area += 1
                    stack.append((nx, ny))
    return area

result = []
cnt = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] != 1 and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            result.append(dfs(i, j))

result.sort()

print(cnt)
print(*result)