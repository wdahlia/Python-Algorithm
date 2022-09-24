
import sys
sys.stdin = open('2884.txt')

# 45분 일찍 알람 설정하기

hour, minute = map(int, input().split())

if minute < 45:
    if hour == 0:
        hour = 23
        minute = (minute - 45) + 60
    else:
        hour -= 1
        minute = (minute - 45) + 60

else:
    minute = minute - 45

print(hour, minute)
