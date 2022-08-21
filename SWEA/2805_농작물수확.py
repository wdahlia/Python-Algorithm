
import sys
sys.stdin = open('2805.txt')

# N // 2 행, 열 모두

T = int(input())


for i in range(1, T+1):

    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    print(farm)

    result = 0
    point = N // 2
    s, a = point, point
    
    for r in range(N):
        for c in range(s, a+1):
            result += farm[r][c]

        if r < point:
            s -= 1
            a += 1
        else:
            s += 1
            a -= 1

    print(f'#{i} {result}')

            
        