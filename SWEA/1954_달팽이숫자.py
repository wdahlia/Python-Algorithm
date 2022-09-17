
import sys
sys.stdin = open('1954.txt')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    x, y = 0, -1
    dir = 1
    cnt = 0

    while N:
        for _ in range(N):
            y += dir
            cnt += 1
            matrix[x][y] = cnt
        
        N -= 1

        for _ in range(N):
            x += dir
            cnt += 1
            matrix[x][y] = cnt

        dir *= (-1)

    print(f'#{i}')
    
    for row in matrix:
        print(*row, sep=' ')


        
        


