
import sys
sys.stdin = open('1100.txt')

matrix = [list(input()) for _ in range(8)]

w_horse = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if matrix[i][j] == 'F':
                w_horse += 1

print(w_horse)
