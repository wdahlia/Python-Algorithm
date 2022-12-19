
import sys
sys.stdin = open('10026.txt')

# 적록색약, 빨,초의 차이를 느끼지 못한다
# 적록색약이 아닌 사람이 봤을 때와, 아닌 사람이 봤을때의 구역을

N = int(input())
matrix = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(color, i, j):
    global colorCnt

    colorCnt = 1
    visited[i][j] = True
    stack = [(color, i, j)]

    while len(stack) != 0:
        c, x, y = stack.pop()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if -1 < nx < N and -1 < ny < N:
                if c == matrix[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    colorCnt += 1
                    stack.append((matrix[nx][ny], nx, ny))

    return colorCnt
                    

result = []
colorCnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            result.append(dfs(matrix[i][j], i, j))

print(len(result), end=" ")

# 적록색약
visited = [[False] * N for _ in range(N)]

for k in range(N):
    for l in range(N):
        if matrix[k][l] == 'R':
            matrix[k][l] = 'G'

result = []
colorCnt = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            result.append(dfs(matrix[r][c], r, c))

print(len(result))

        
