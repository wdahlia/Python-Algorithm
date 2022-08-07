import sys
sys.stdin = open('1236_성지키기.txt')
# '.'는 빈칸 'X'는 경비원
# 모든 행과 모든 열에 한명 이상의 경비원

N, M = list(map(int, input().split())) # 성의 행(N)과 열(M)의 크기가 주어짐

matrix = [list(input()) for _ in range(N)]

n = 0
cnt = 0
for i in range(N): 
    if 'X' not in matrix[i]:
        cnt += 1

n = 0
for j in range(M):
    num = 0
    for i in range(N):
        if matrix[i][j] == 'X':
            break
        else:
            num += 1
    if num == N:
        n += 1


print(max(n, cnt))
    
