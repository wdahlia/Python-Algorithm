
import sys
sys.stdin = open('1012.txt')
def dfs(x, y):
    global cnt

    stack = [(x, y)]

    while len(stack) != 0:
        x, y = stack.pop()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < N and 0<= ny < M:
                if matrix[nx][ny] != 1:
                    continue
                if visited[nx][ny] == True:
                    continue
                else:
                    visited[nx][ny] = True
                    cnt += 1
                    stack.append((nx, ny))

    return cnt

# 우 하 좌 상 - 좌표 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for _ in range(T):

    N, M, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        r, c = map(int, input().split())
        matrix[r][c] = 1                     # 좌표값에 1 넣어준다

    result = []
    cnt = 0
    for i in range(N):                       
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] != True:
                visited[i][j] = True                            # i와 j는 좌표값
                result.append(dfs(i, j))
                
    print(len(result))
