
import sys
sys.stdin = open('4396.txt')

from pprint import pprint

N = int(input())

matrix = [list(input()) for _ in range(N)]
matrix1 = [list(input()) for _ in range(N)]

for row in range(8):
    for col in range(8):
        if matrix[row][col] == '.' and matrix1[row][col] == 'x':
            print()
