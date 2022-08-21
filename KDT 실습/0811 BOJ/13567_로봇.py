
import sys
sys.stdin = open('13567.txt')

from pprint import pprint

# 왼쪽 아래 부터 시작 즉, 주어진 행이 있다면 (M-1, 0)의 좌표값이 (0, 0) 이 됨
# n은 n개의 명령어가 주어짐
# TURN 0 현재위치 왼쪽 90도 회전 즉, 위로 이동 행 인덱스 + 1
# TURN 1 현재위치 오른쪽 90도 회전 즉, 아래로 이동 행 인덱스 - 1
# MOVE d d만큼 움직임 

M, N = map(int, input().split())

matrix = [[0] * (M+1) for _ in range(M+1)]

for i in range(M+1):
    for j in range(M+1):
        matrix[i][j] = [M-i, j]

# 사방탐색을 하면서 사방탐색을 변화 시켜야할듯
# 즉, move 0을 만나면 dy, dx = dx, dy로
# move 1

switch = True
dx = [0, 0] # 좌우
dy = [-1, 1]

x, y = M, 0
turn = 1
for _ in range(N):
    command, mv = input().split()
    mv = int(mv)
    

    if command == 'MOVE':
        nx = x + (dx[i] * mv)
        ny = y + (dy[i] * mv)
        if -1 < nx <= M and -1 < ny <= M:
            x = nx
            y = ny
        else:
            switch = False
            break
    else:
        if command == 'TURN':
            if mv == 0:
                dx[0], dx[1] = dy[0], dy[1]
            else:
                dx[0], dx[1] = dy[1], dy[0]

if switch:
    print(matrix[x][y])
else:
    print(-1)





 




