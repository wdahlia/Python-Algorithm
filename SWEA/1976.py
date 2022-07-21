# import sys
# sys.stdin = open('1976.txt', 'r')

T = int(input())
for i in range(1, T+1):
    time = list(map(int, input().split()))
    h = time[0] + time[2]
    m = time[1] + time[3]
    if h > 12:
        h -= 12
    if m > 59:
        m -= 60
        h += 1
    print(f'#{i} {h} {m}')