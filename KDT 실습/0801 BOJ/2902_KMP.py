
import sys
sys.stdin = open('2902.txt')

# 사람 성이 들어간 알고리즘 두 가지 형태
# 긴 형태
# Knuth-Morris-Pratt 
# 짧은 형태
# KMP
# 긴 형태의 알고리즘 > 짧은 형태로 바꾸어 출력

# split을 '-'로 해서 upper인것만 출력 하는 방법
made_algorithm = input().split('-')

for madeby in made_algorithm:
    print(madeby[0], end='')

# 아스키 코드 활용
madeby = input()

length = len(madeby)

for idx in range(length):
    if 65 <= ord(madeby[idx]) <= 90:
        print(madeby[idx], end = '')
        