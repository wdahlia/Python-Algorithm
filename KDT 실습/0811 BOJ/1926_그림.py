'''
output
4
9
'''
# 큰 도화지에 그림 그려져 있을 때
# 그림의 개수
# 그림 중 max 넓이 출력
# 1로 연결된 것을 그림
# 가로 세로는 연결 o, 대각선 연결은 x

# 델타 탐색, bfs 같이 쓴다

from pprint import pprint 
import sys

sys.stdin = open('1926.txt')

v, h = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(v)]
visited = [[False] * h for _ in range(v)]


dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]


def dfs(x, y):
    area = 1
    stack = [(x, y)]
    visited[x][y] = True

    while len(stack) != 0:
        a, b = stack.pop()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < v and 0 <= ny < h:
                if visited[nx][ny] == False and matrix[nx][ny] == 1:
                    area += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))
            else:
                continue
                
    return area


result = []
for r in range(v):
    for c in range(h):
        if matrix[r][c] == 1 and visited[r][c] == False:
            result.append(dfs(r, c))

print(result)
print(len(result))

if len(result) == 0:
    print(0)
else:
    print(max(result))
