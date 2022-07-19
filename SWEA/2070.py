
import sys
sys.stdin = open('2070.txt', 'r')

T = int(input())
for i in range(1, T+1):
    x, y = map(int, input().split())
    if x > y:
        print(f'#{i} >')
    elif x < y:
        print(f'#{i} <')
    else:
        print(f'#{i} =')
