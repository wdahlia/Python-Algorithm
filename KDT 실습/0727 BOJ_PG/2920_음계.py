
import sys
sys.stdin = open('2920.txt')

d_major = list(map(int, input().split()))

# 방법 1 - 비교 리스트를 직접 만들어 비교
compare_d = [1,2,3,4,5,6,7,8]           # 비교할 리스트를 구성해준다

if d_major == compare_d:                # 비교 리스트와 같으면 ascending 출력
    print('ascending')
elif d_major == compare_d[::-1]:        # 비교 리스트의 역순과 같으면 descending 출력
    print('descending')
else:                                   # 나머지는 mixed 출력
    print('mixed')

# 방법 2 - d_major를 sorted한 함수와 비교하는 것

if d_major == sorted(d_major):                 # 올림차순
    print('ascending')
elif d_major == sorted(d_major, reverse=True): # 내림차순
    print('descending')
else:
    print('mixed')
