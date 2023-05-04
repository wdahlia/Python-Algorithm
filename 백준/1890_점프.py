from collections import deque
from pprint import pprint
import sys
sys.stdin = open('1890.txt')

# 오른쪽이나 아래로만 이동해야함
# 0은 종착점
# 규칙에 맞게 이동할 수 있는 경로의 개수 구하는 프로그램 작성
# bfs, dfs 가능하고, dp도 가능?

# bfs 메모리 초과
def bfs(i, j, jmp, count):

    queue = deque([(i, j, jmp)])

    while queue:
        x, y, jump = queue.popleft()
        for idx in range(2):
            nx = x + (dx[idx] * jump)
            ny = y + (dy[idx] * jump)
            if nx < N and ny < N and not visited[nx][ny]:
                queue.append((nx, ny, matrix[nx][ny]))
            
            if nx == N-1 and ny == N-1:
                visited[nx][ny] += visited[i][j]
                break

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [0, 1] # 오른쪽, 아래
dy = [1, 0]

visited[0][0] = 1
bfs(0, 0, matrix[0][0], 0)
print(visited[N-1][N-1] - 1)


# dp풀이

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        
        if i == N-1 and j == N-1:
            print(dp[i][j])
            break

        if j + matrix[i][j] < N:
            dp[i][j + matrix[i][j]] += dp[i][j]

        if i + matrix[i][j] < N: 
            dp[i + matrix[i][j]][j] += dp[i][j]

