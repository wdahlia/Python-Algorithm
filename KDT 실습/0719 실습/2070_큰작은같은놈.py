
# 2개의 수를 입력 받아 크기를 비교, 등호 부등호를 출력
# input : 3 8 ; output : < 
# import sys
# sys.stdin = open('2070.txt', 'r')

T = int(input())
for i in range(1, T+1):
    x, y = map(int, input().split())
    if x > y: # x가 클 때
        print(f'#{i} >')
    elif x < y: # y가 클 때
        print(f'#{i} <')
    else: # 같을 경우
        print(f'#{i} =')
