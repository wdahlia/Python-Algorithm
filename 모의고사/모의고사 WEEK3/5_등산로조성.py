import sys
from unittest.util import _MAX_LENGTH

sys.stdin = open("_등산로조성.txt")

from pprint import pprint

# 등산로 조성 N * N
# 등산로 가장 높은 봉우리에서 시작 max 값
# 높은 > 낮은 가로 세로 상하좌우 델타탐색
# 딱 한 곳을 정해서 최대 K 깊이만큼 지형 깎는 공사
# 제일 긴 등산로 만들어야함... length += 1씩해서 이걸 append 해주어야함 막힐때까지
# 아 9, 9 이런 애들은 K가 안주어진다면 생략하고 넘어가야함

T = int(input())

for _ in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [(list(map(int, input().split()))) for _ in range(N)]
    visited = [[False] * N for _ in range(N)] # 방문 리스트

    top = 0 # max 값 찾아준다
    for r in range(N):
        for c in range(N):
            if matrix[r][c] > top :
                top = matrix[r][c]


    
                

    dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    def dfs(x, y):
            global top
            length = 1
            stack = [(x, y)]

            while len(stack) != 0:
                row, col = stack.pop()

                for idx in range(4):
                    nx = row + dx[idx]
                    ny = col + dy[idx]

                    if -1 < nx < N and -1 < ny < N:
                        if visited[nx][ny] != True and visited[nx][ny] <= top:
                            if top == visited[nx][ny]:
                                if 1 <= K <= 5:
                                    visited[nx][ny] = visited[nx][ny] - K
                                    top = visited[nx][ny]
                                    K = 0
                                else:
                                    break
                            else:
                                visited[nx][ny] = True
                                top = visited[nx][ny]
                                length += 1
                                stack.append((nx, ny))
                        else:
                            break

            return length 

    result = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == top and visited[i][j] != True:
                visited[i][j] = True
                result.append(dfs(i, j))

    print(result)



