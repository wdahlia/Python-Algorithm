
import sys
sys.stdin = open('2468.txt')

# 물에 잠기지 않는 안전한 영역 최대로 몇 개?
# 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠김
# 상하좌우로 인접해 있고, 그 크기가 최대인 영역을 말함

from pprint import pprint
input = sys.stdin.readline

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def dfs(x, y, h):

    visited[x][y] = True
    
    stack = [(x, y)]

    while stack:
        r, c = stack.pop()
        for idx in range(4):
            nx = r + dx[idx]
            ny = c + dy[idx]
            if -1 < nx < N and -1 < ny < N:
                if spotMatrix[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    


N = int(input())

spotMatrix = []
minHeight = 100
maxHeight = 0
for _ in range(N):
    spot = list(map(int, input().split()))
    minHeight = min(minHeight, min(spot))
    maxHeight = max(maxHeight, max(spot))
    spotMatrix.append(spot)


result = 0
for k in range(minHeight, maxHeight+1):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if spotMatrix[i][j] > k and not visited[i][j]:
                cnt += 1
                dfs(i, j, k)

    result = max(result, cnt)

if result == 0: # 아무것도 물에 잠기지 않는 경우
    result = 1

print(result)
