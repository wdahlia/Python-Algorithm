
import sys
sys.stdin = open('4396.txt')

from pprint import pprint

# n개의 줄 지뢰의 위치
# '.'는 지뢰가 없는 지점, '*' 지뢰가 있는 지점
# 열린 칸은 x, 열리지 않는 칸 .
# 열린 칸에는 0과 8 사이의 숫자
# 지뢰 있는 칸 열렸다면 지뢰가 있는 모든 칸이 별표로 표시

# 8방향 탐색
# cnt를 해주어야함, 지뢰가 8방향 안에 있는 경우 지뢰 cnt + 1씩

N = int(input())
matrix = [list(input()) for _ in range(N)]
matrix1 = [list(input()) for _ in range(N)]

zero = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0, -1, 1, -1, 1] 
dy = [0, 0, -1, 1, -1, -1, 1, 1]

switch = False
for r in range(N):
    for c in range(N):
        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == '*' and matrix1[r][c] == 'x':
                    zero[r][c] += 1
                
        if matrix1[r][c] == '.':
            zero[r][c] = '.'
            
        if matrix[r][c] == '*':
            if matrix1[r][c] == 'x':
                switch = True

if switch == True:
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '*':
                zero[r][c] = '*'

for row in zero:
    print(*row, sep='')