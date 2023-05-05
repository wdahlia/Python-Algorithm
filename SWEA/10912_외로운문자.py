
import sys
sys.stdin = open('10912.txt')

# 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램
# 남는 문자는 사전 순서대로 출력

T = int(input())

for tc in range(1, T+1):
    words = input()
    dict = {}

    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    
    res = ''
    for k, v in dict.items():
        if v % 2:
            res += k
    
    if res == '':
        res = 'Good'
    else:
        res = ''.join(sorted(res))

    print(f'#{tc} {res}')