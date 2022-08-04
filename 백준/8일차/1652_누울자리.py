import sys
sys.stdin = open('1652_누울자리.txt')

# 연속으로 2칸 이상의 빈칸 존재하면 가로 세로든 누울 수 있음
# 단, 중간에는 못 누움 벽이나 짐이 있어야 함
# '.' 는 빈칸 'X'는 짐
# print는 가로 세로 누울 수 있는 자리의 수

T = int(input())

matrix = [list(input()) for _ in range(T)]


num_row = 0
for row in range(T):
    rc_cnt = 0
    for col in range(T):
        if matrix[row][col] == '.':
            rc_cnt += 1

        else:
            if rc_cnt >= 2:
                num_row += 1
                rc_cnt = 0
            else:
                rc_cnt = 0 
    
    if rc_cnt >= 2:
        num_row += 1

num_col = 0
for row in range(T):
    cr_cnt = 0
    for col in range(T):
        if matrix[col][row] == '.':
            cr_cnt += 1
        
        elif matrix[col][row] == 'X':
            if cr_cnt >= 2:
                num_col += 1
                cr_cnt = 0
            else:
                cr_cnt = 0

    if cr_cnt >= 2:
        num_col += 1


print(num_row, num_col)