
import sys
sys.stdin = open('2638.txt')

# 4변중에 2변 이상이 실내공기와 접촉한 것은 한시간 만에 녹아 없어짐
# 모두 녹아 없어지는데 걸리는 시간을 구하는 프로그램 작성
# 두변이 모두 0과 마주치는 애들을 cnt해주고 +1을 해주면됨

from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def dfs(i, j):
    visited[i][j] = 1
    stack = [(i, j)]
    
    while len(stack) != 0:
        x, y = stack.pop()
        
        dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
        dy = [0, 0, -1, 1]

        cnt = 0
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if -1 < nx < N and -1 < ny < M:
                if matrix[nx][ny] == 0 and visited[nx][ny] == 2:
                    continue
                elif matrix[nx][ny] == 0:
                    cnt += 1

                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
                    visited[nx][ny] = 0
                    
        if cnt >= 2:
            visited[x][y] = 2
            matrix[x][y] = 0


hour = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            hour += 1
            print(i, j)
            dfs(i, j)

print(hour)