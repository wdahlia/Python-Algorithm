
import sys
sys.stdin = open('4963.txt')

def dfs(x, y):
    visited[x][y] = True

    dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    stack = [(x, y)]

    while len(stack) != 0:
        r, c = stack.pop()
        for idx in range(8):
            nx = r + dx[idx]
            ny = c + dy[idx]
            if -1 < nx < h and -1 < ny < w:
                if mapboard[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))


while 1:
    w, h = map(int, input().split())

    mapboard = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    if w == 0 and h == 0:
        break

    cnt = 0
    for i in range(h):
        for j in range(w):
            if mapboard[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)
