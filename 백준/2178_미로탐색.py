
import sys
sys.stdin = open('2178.txt')

from collections import deque

# 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸을 나타냄
# (1,1)에서부터 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸수를 구하는 프로그램 작성
# 최소 칸 수 즉, 단거리 이동을 의미


def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        i, j = queue.popleft()

        if i == N-1 and j == M-1:
            print(graph[i][j])
            break

        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if -1 < nx < N and -1 < ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[i][j] + 1
                    queue.append((nx, ny))



    
N, M = map(int, input().split()) # n은 행, m은 열
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

bfs()