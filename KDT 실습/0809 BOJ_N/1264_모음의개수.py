
import sys
sys.stdin = open('1264.txt')

# 영문 문장 모음의 개수 세는 프로그램

while 1:
    cnt = 0
    sentence = input()
    if sentence == '#':
        break
    for char in sentence:
        if char in 'aeiouAEIOU':
            cnt += 1

    print(cnt)
    