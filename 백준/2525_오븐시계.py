
import sys
sys.stdin = open('2525.txt')

# 현재시각
# 요리에 필요한 시각

hour, minute = map(int, input().split())
cookingTime = int(input())

totalMinute = minute + cookingTime 
if totalMinute >= 60:
    while totalMinute >= 60:
        hour += 1
        if hour == 24:
            hour = 0
        totalMinute -= 60
    minute = totalMinute
    
else:
    minute = totalMinute

print(hour, minute)
    


