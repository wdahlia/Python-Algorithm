
import sys
from collections import deque
sys.stdin = open('16918.txt')

# 격자의 각 칸은 비어있거나 폭탄이 들어있다.
# 폭탄이 폭발하면 상하좌우 파괴
# 인접한 칸에 폭탄 있으면 폭발 없이 그냥 파괴


R, C, N = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]
queue = deque()

def bfs(q, arr):
    while q:
        x, y = q.popleft()
        arr[x][y] = '.'
        for indx in range(4):
            nx = x + dx[indx]
            ny = y + dy[indx]
            if -1 < nx < R and -1 < ny < C and arr[nx][ny] == 'O':
                arr[nx][ny] = '.'

def bomberman(time):
    global queue, matrix

    if time == 1:
        # 1초 일때
        # 모든 칸에 폭탄 설치
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 'O':
                    # 폭탄 폭발시킬때 주변 상하좌우 파괴해야함으로 인덱스 기억해두어야함
                    queue.append((i, j))

    elif time % 2:
        # 3초 지났을때는 폭파시켜야함
        bfs(queue, matrix)
        # 다시 폭탄을 큐에 저장
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 'O':
                    queue.append((i, j))

    
    else:
        matrix = [['O'] * C for _ in range(R)]


for t in range(1, N+1):
    bomberman(t)

for i in range(R):
    print(''.join(matrix[i]))