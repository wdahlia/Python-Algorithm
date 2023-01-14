
import sys
sys.stdin = open('1913.txt')

from pprint import pprint
# 1 1 -1 -1

N = int(input())
num = int(input())

matrix = [[0] * N for _ in range(N)]

row = -1
col = 0
dir = 1

numArray = []
cnt = N ** 2
while cnt:
    for _ in range(N):
        row += dir
        matrix[row][col] = cnt
        cnt -= 1
        if matrix[row][col] == num:
            numArray.append(row + 1)
            numArray.append(col + 1)
       

    for _ in range(N-1):
        col += dir
        matrix[row][col] = cnt
        cnt -= 1
        if matrix[row][col] == num:
            numArray.append(row + 1)
            numArray.append(col + 1)


    N -= 1
    dir *= -1

for result in matrix:
    print(*result)

print(*numArray)