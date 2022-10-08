
import sys
sys.stdin = open('2615.txt')

from pprint import pprint
# 19개 가로줄, 19개 세로줄
# 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이김
# 가로, 세로, 대각선 전부 다
# 여섯 알 이상이 연속적으로 놓인 경우는 이긴 것 X (예외)
# 누가 이겻는지 승부 결정 안되었는지 판단
# 검 1, 흰 2, 알 x 0
# 가장 위에 있는 것의 가로줄 번호와 세로줄 번호

                             
board = [list(map(int, input().split())) for _ in range(19)]

def omok():

    dx = [-1, 0, 1, 1] # 우상 우 우하 하 
    dy = [1, 1, 1, 0]

    for x in range(19):
        for y in range(19):
            if board[x][y] == 1 or board[x][y] == 2:
                for idx in range(4):
                    cnt = 1
                    nx = x + dx[idx]
                    ny = y + dy[idx]

                    while -1 < nx < 19 and -1 < ny < 19 and board[nx][ny] == board[x][y]:
                        cnt += 1
                        
                        if cnt == 5:
                            if -1 < nx + dx[idx] < 19 and -1 < ny + dy[idx] < 19 and board[nx][ny] == board[nx + dx[idx]][ny + dy[idx]]:
                                break
                            if -1 < x - dx[idx] < 19 and -1 < y - dy[idx] < 19 and board[x][y] == board[x - dx[idx]][y - dy[idx]]:
                                break
                            return board[x][y], x+1, y+1
                                
                        nx += dx[idx]
                        ny += dy[idx]

    return 0, 0, 0
                                
win, x, y = omok()

if win == 0:
    print(win)
else:
    print(win)
    print(x, y)