import sys
sys.stdin = open('5063_TGN.txt')


T = int(input())

for _ in range(T):
    r, e, c = list(map(int, input().split()))

    if r == e-c:
        print('does not matter')
    elif r < e-c:
        print('advertise')
    else:
        print('do not advertise')