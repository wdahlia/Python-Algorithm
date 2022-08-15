
import sys
sys.stdin = open('2167.txt')

n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
    i, j, x, y = list(map(int, input().split()))
    sum_result = 0
    for row in range(i-1, x):
        for column in range(j-1, y):
            sum_result += matrix[row][column]
    
    print(sum_result)
