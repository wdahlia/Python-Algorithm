
import sys
sys.stdin = open('2578.txt')

from pprint import pprint

# 행, 열, 대각선 cnt 체크
check_bingo = [0] * 12

board = []
winning_num = []

# 빙고판 입력
for _ in range(5):
    array = list(map(int, input().split()))
    board.append(array)

# 사회자가 부르는 숫자
for _ in range(5):
    winning_num += list(map(int, input().split()))

switch = True
result = 0
for n in range(25):
    if switch:
        for i in range(5):
            for j in range(5):
                if winning_num[n] == board[i][j]:
                    check_bingo[i] += 1 # 행 cnt 체크
                    check_bingo[j+5] += 1 # 열 cnt 체크
                    if i == j:
                        check_bingo[10] += 1 # 대각선
                    if i + j == 4:
                        check_bingo[11] += 1 # 역대각선

                    if check_bingo.count(5) >= 3:
                        print(n+1)
                        switch = False
                        break
