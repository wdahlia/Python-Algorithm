
# input
'''
3
0 10
33 1005
1 4
'''
# output : 
'''
2
199
0
'''

import sys
sys.stdin = open('11170.txt')

T = int(input()) # test case 개수

for _ in range(T):
    cnt = 0 # 각 케이스마다 cnt를 초기화
    N, M = list(map(int, input().split())) # N, M을 받아줌
    for i in range(N, M+1): # M까지 0의 개수 세야하므로 M+1을 해준다
        char = str(i) # 문자열로 바꾸어야지 10 도 1 0 이렇게 탐색 가능
        if '0' in char: # char안에 0이 있다면
            zero = char.count('0') # 0의 개수를 세서 zero에 할당
            cnt += zero # zero를 cnt에 넣어주자
    print(cnt) # 모든 for문이 끝나면 cnt를 출력
