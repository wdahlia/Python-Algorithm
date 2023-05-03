
import sys
sys.stdin = open('15230.txt')

T = int(input())

compare_alphs = 'abcdefghijklmnopqrstuvwxyz'

for tc in range(1, T+1):
    alphs = input()

    idx = 0
    word = alphs[idx]
    res = 0
    while 1:
        if word == compare_alphs[:idx+1] and idx != len(alphs) - 1:
            idx += 1
            word += alphs[idx]
            continue
        else:
            if word == compare_alphs[:idx+1]:
                res = len(word)
            else:
                res = len(word) - 1
            print(f'#{tc} {res}')
            break