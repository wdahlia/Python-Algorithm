
import sys
sys.stdin = open('11403.txt')

# 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재
# 0인 경우는 없다는 뜻
# i번째 줄의 i번째 숫자는 항상 0이다.

from collections import deque


def bfs(num):

    queue = deque([num])
    visited = [0] * N

    while queue:
        x = queue.popleft()
        for n in graph[x]:
            if not visited[n]:
                visited[n] = 1
                queue.append(n)
    print(*visited)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            graph[i].append(j)


for num in range(N):
    bfs(num)
