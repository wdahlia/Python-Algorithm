import sys
sys.stdin = open('1989.txt', 'r')


T = int(input())
for i in range(1, T+1):
    word = input()
    if word == word[::-1]:
        end = 1
    else:
        end = 0
    print(f'#{i} {end}')