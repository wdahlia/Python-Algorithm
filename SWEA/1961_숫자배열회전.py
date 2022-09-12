
import sys
sys.stdin = open('1961.txt')

from pprint import pprint

T = int(input())

for idx in range(1, T+1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]
    
    matrix1 = [[0] * N for _ in range(N)]
    matrix2 = [[0] * N for _ in range(N)]
    matrix3 = [[0] * N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            matrix1[j][N-i-1] = matrix[i][j]
            matrix2[N-i-1][N-j-1] = matrix[i][j]
            matrix3[N-j-1][i] = matrix[i][j]

    print(f'#{idx}', end='\n')
    for k in range(N):
        result = ''
        result += ''.join(matrix1[k])
        result += ' '
        result += ''.join(matrix2[k])
        result += ' '
        result += ''.join(matrix3[k])

        print(result)
            
    