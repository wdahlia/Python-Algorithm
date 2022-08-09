
# 입력된 숫자가 N일때 거꾸로 출력하는 예시
# input : 8 ; output : 8 7 6 5 4 3 2 1 0
# import sys
# sys.stdin = open('1545.txt', 'r')

n = int(input())
while n >= 0: # n이 0보다 크거나 같을 때까지, 즉 n이 0 미만이면 종료
    print(n, end=' ') # n 출력해준다
    n -= 1 # n은 1씩 감소
