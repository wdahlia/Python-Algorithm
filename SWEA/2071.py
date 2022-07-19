# import sys
# sys.stdin = open('2071.txt', 'r')

T = int(input())
for i in range(1, T+1):
    a = list(map(int, input().split()))
    if a:
        b = sum(a[::])/10
        print(f'#{i} {round(b)}')
        