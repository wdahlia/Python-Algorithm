
import sys 
sys.stdin = open("1018.txt")

from pprint import pprint

# 검은색 흰색 각각 칸 하나로 칠해져있음
# 변을 공유하는 친구는 다른 색으로 칠해져야 함

def search(x, y):
    global cnt1
    global cnt2

    copy = [item[:] for item in matrix]

    if matrix[x][y] != 'W':
        cnt1 += 1
        copy[x][y] = 'W'

    for r in range(x, x+8):
        for c in range(y, y+8):
            if -1 < r <= N and -1 < c <= M:
                for idx in range(2):
                    nx = r + dx[idx]
                    ny = c + dy[idx]
                    if -1 < nx < x+8 and -1 < ny < y+8:
                        if copy[r][c] == copy[nx][ny]:
                            cnt1 += 1
                            if copy[nx][ny] == 'W':
                                copy[nx][ny] = 'B'
                            else:
                                copy[nx][ny] = 'W' 

    copy = [item[:] for item in matrix]

    if matrix[x][y] != 'B':
        cnt2 += 1
        copy[x][y] = 'B'

    for r in range(x, x+8):
        for c in range(y, y+8):
            if -1 < r <= N and -1 < c <= M:
                for idx in range(2):
                    nx = r + dx[idx]
                    ny = c + dy[idx]
                    if -1 < nx < x+8 and -1 < ny < y+8:
                        if copy[r][c] == copy[nx][ny]:
                            cnt2 += 1
                            if copy[nx][ny] == 'B':
                                copy[nx][ny] = 'W'
                            else:
                                copy[nx][ny] = 'B' 

    
                    
    return min(cnt1, cnt2)



dx = [1, 0] # 우, 하
dy = [0, 1]

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
result = []

for i in range(N-7):
    for j in range(M-7):
        cnt1 = cnt2 = 0
        result.append(search(i, j))


print(min(result))
