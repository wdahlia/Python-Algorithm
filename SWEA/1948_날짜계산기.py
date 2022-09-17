
import sys
sys.stdin = open('1948.txt')

# 월 일로 이루어진 날짜 2개 입력, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력

month_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

T = int(input())

for i in range(1, T+1):
    month1, day1, month2, day2 = map(int, input().split())
    
    result = 0
    for m in range(month1, month2):
        if m == month1:
            result += month_day[m] - day1 + 1
        else:
            result += month_day[m]
    result += day2

    print(f'#{i} {result}')
