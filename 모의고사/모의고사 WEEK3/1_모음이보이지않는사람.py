
import sys
sys.stdin = open("_모음이보이지않는사람.txt")

# 모음이 다 사라졌음
# congratulation cngrtltn

# replace 함수 이용
T = int(input())
for n in range(1, T+1):
    word = input()

    for alph in 'aeiou':
        if alph in word:
            word = word.replace(alph, '')
    
    print(f'#{n} {word}')

# for문으로 문자열에 추가해주는 방법있음
T = int(input())
for n in range(1, T+1):
    word = input()

    result = ''
    for alph in word:
        if alph == 'a':
            continue
        elif alph == 'e':
            continue
        elif alph == 'i':
            continue
        elif alph == 'o':
            continue
        elif alph == 'u':
            continue
        else:
            result += alph
    
    print(f'#{n} {result}')
