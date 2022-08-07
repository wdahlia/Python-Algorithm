import sys
sys.stdin = open('2167_2차원배열의합.txt')

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

            


# matrix1 = []
# for _ in range(n+1):
#     matrix1.append([0] * (m+1))

# for i in range(n):
#     for j in range(1, m+1):
#         matrix1[i][j] = matrix[i-1][j-1] + matrix1[i


# print(matrix1)



    # matrix[i][j]