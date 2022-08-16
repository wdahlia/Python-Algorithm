
import sys
sys.stdin = open('11945.txt')

# 슬라이싱 이용 72ms
N, M = map(int, input().split())

for _ in range(N):
    bread = input()[::-1]
    print(bread)

# 뒤집어준다 72ms
N, M = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]

new = [[0] * M for _ in range(N)]

for i in range(N):
    bread = ''
    for j in range(M):
        new[i][j] = matrix[i][M-1-j]
        bread += str(new[i][j])
    print(bread)

# 문자열 길이 사용 68ms
N, M = map(int, input().split())

for i in range(N):
    result = input()
    bread = ''
    l = len(result)
    for i in range(l):
        bread += result[l-1-i]
        print(bread)
    print(bread)
