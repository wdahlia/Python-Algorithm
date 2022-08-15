
import sys
sys.stdin = open('5533.txt')

# 게임을 3번 했다고 했으므로 열의 개수 3
# 행의 개수는 input받은 N의 개수일 것

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]


gamescore = [[], [], []]
for c in range(3):
    for r in range(N):
        gamescore[c].append(matrix[r][c])
    

for c in range(3):
    for r in range(N):
        if gamescore[c].count(matrix[r][c]) >= 2:
            matrix[r][c] = 0

for r in range(N):
    print(sum(matrix[r]))
