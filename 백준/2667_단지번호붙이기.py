
import sys
sys.stdin = open('2667.txt')

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


def dfs(i, j):
    houseNum = 1
    visited[i][j] = True
    stack = [(i, j)]

    while len(stack) != 0:
        x, y = stack.pop()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if -1 < nx < N and -1 < ny < N:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    houseNum += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    return houseNum


houseNums = []
blockCnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            blockCnt += 1
            houseNums.append(dfs(i, j))
            
houseNums.sort()
print(blockCnt)
print(*houseNums, sep="\n")