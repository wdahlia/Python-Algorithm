import sys
sys.stdin = open('소득불균형.txt')

T = int(input())

for i in range(1, T+1):
    case_n = int(input())

    income_n = list(map(int, input().split()))

    sum_income = sum(income_n) # income_n을 sum해준다.

    cnt = 0 #cnt = 0
    for person in income_n:
        if person <= (sum_income // case_n): # sum_income을 case_n 즉, 주어진 문자 숫자로 나누어서 
            cnt += 1                         # 평균을 구하고 person이 평균보다 작거나 같다면 cnt += 1
    print(f'#{i} {cnt}')
        



