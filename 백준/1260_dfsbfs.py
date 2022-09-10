
import sys
sys.stdin = open('1260.txt')

from collections import deque

# 정점의 개수 N
# 간선의 개수 M
# 탐색시작 정점의 번호 V
# 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
N, M, V = map(int, input().split())
graph = [[] for _ in range(M+1)] 
visited = [False] * (M+1)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(M+1):
    graph[i].sort()



def dfs(start):
    visited[start] = True
    stack = [start]
    # print(start, end=' ')

    while len(stack) != 0:
        point = stack.pop()

        for current in graph[point]:
            # print(current)
            if not visited[current]:
                visited[current] = True
                stack.append(current)
                print(stack)
dfs(V)
