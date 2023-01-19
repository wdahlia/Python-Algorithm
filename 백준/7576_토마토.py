
import sys
sys.stdin = open('7576.txt')

# 익은 토마토의 영향을 받아 익게 됨
# 상하좌우에 있는 토마토에 영향 받음
# 몇일이 지나면 다 익게되는지 최소일수를 알고싶음
# 토마토가 안 들어있는 경우도 있음
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸
# 모든 토마토가 익어있는 상태이면 0을 출력, 모두 익지는 못하는 상황이면 -1을 출력

from collections import deque
from pprint import pprint

def bfs():
    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if -1 < nx < N and -1 < ny < M:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[i][j] + 1
                    queue.append((nx, ny))



M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
result = 0
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1: # queue에 1인 애들을 모두다 먼저 넣어놓고 bfs를 실행
            queue.append((r, c))

bfs()

for row in range(N):
    for col in range(M):
        if matrix[row][col] == 0:
                print(-1)
                exit(0)

        result = max(result, matrix[row][col])

print(result - 1)
