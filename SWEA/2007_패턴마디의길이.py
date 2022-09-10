
import sys
sys.stdin = open('2007.txt')

# 슬라이싱으로 풀이
# 마디 최대 길이 10

T = int(input())

for idx in range(1, T+1):
    sentence = input()
    for i in range(1, 11):
        word = sentence[:i]
        repeat = sentence[i:2*i]
        if word == repeat:
            print(f'#{idx} {i}')
            break
