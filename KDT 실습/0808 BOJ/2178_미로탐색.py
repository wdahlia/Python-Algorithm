
import sys
sys.stdin = open('2178.txt')

from collections import deque

from pprint import pprint

'''
output
38
'''

# 1은 이동할 수 잇는 칸, 0은 이동할 수 없는 칸
# (n,m)의 위치로 이동할 때 지나야 하는 최소 칸 수를 구하는 프로그램 작성
# 서로 인접한 칸으로 이동
# 칸을 세는 것에는 시작 위치와 도착 위치도 포함
# 상,하,좌,우 - 좌표값


def bfs(matrix, i, visited):
    queue = deque()
    queue.append(i)

    while queue:
        value = queue.popleft()
        if not visi
    

N, M = map(int, input().split())
dx = [-1, 1, 0, 0]                 # 상, 하, 좌, 우
dy = [0, 0, -1, 1]
matrix = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

result = []
cnt = 1
for r in range(N):
    for c in range(M):
        for idx in range(4):
            nx = r + dx[idx]
            ny = c + dy[idx]
            if -1 < nx < N and -1 < ny < M:
                if matrix[nx][ny] == '1' and not 1:
                    cnt += 1
                    mat
