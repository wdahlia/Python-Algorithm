
import sys
sys.stdin = open('4047.txt')

# 겹치는 카드 있으면 ERROR
# S, D, H, C 각 카드의 무늬에서 부족한 카드의 숫자 출력
# 카드 개수 총 13개

T = int(input())

for tc in range(1, T+1):
    res = ''
    dict = {'S' : [], 'D' : [], 'H' : [], 'C' : []}
    card_info = input()
    for i in range(0, len(card_info), 3):
        ptn = card_info[i:i+3][0]
        num = int(card_info[i:i+3][1:3])
        if num not in dict[ptn]:
            dict[ptn].append(num)
        else:
            res = 'ERROR'
            break

    print(f'#{tc}', end=' ')

    if res == 'ERROR':
        print(res)
    else:
        for k, v in dict.items():
            print(13 - len(v), end=' ')
        print()

# 통과는 되었는데 영 애매..
