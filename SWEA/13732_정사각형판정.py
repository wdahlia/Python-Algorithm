
import sys
sys.stdin = open('13732.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    dx = [0, 1] # 우, 하
    dy = [1, 0]

    def dfs(r, c):

        stack = [(r, c)]

        cnt = 1

        while stack:
            x, y = stack.pop()
            for idx in range(2):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if -1 < nx < N and -1 < ny < N and not visited[nx][ny] and matrix[nx][ny] == '#':
                    visited[nx][ny] = True
                    cnt += 1
                    stack.append((nx, ny))

        return cnt


    res_array = []
    result = 'yes'

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '#' and not visited[i][j]:
                visited[i][j] = True
                res_array.append(dfs(i, j))

    div = res_array[0] ** 0.5

    if len(res_array) != 1 or (res_array[0] // div) != div:
        result = 'no'
    # elif (res_array[0] // div) == div:
    #     print(res_array[0] // div, div)
    #     result = 'yes'

    print(f'#{tc} {result}')
            
            