
# import sys
# sys.stdin = open('2029.txt', 'r')

T = int(input())
for i in range(1, T+1):
    q, r = map(int, input().split())
    print(f'#{i} {q // r} {q % r}')