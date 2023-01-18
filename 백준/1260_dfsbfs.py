
import sys
sys.stdin = open('1260.txt')

from collections import deque

# 정점의 개수 N
# 간선의 개수 M
# 탐색시작 정점의 번호 V
# 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

# dfs 코드
def dfs(start):
    dfsVisited[start] = True
    stack = [start]
    result.append(start)

    while len(stack) != 0:
        point = stack.pop()

        for current in dfsGraph[point]:
            if not dfsVisited[current]:
                dfsVisited[current] = True # 방문처리를 해준다음 재귀함수 사용해서 그 해당 인덱스 노드 탐색
                dfs(current)

    return result

# bfs 코드 queue를 사용
def bfs(start):
    bfsVisited[start] = True
    array = deque([start])
    result = []
    result.append(start)
    
    while len(array) != 0:
        point = array.popleft()

        for current in bfsGraph[point]:
            if not bfsVisited[current]:
                bfsVisited[current] = True
                array.append(current)
                result.append(current)

    return result


N, M, V = map(int, input().split())
dfsGraph = [[] for _ in range(N+1)] 
dfsVisited = [False] * (N+1)
bfsGraph = [[] for _ in range(N+1)]
bfsVisited = [False] * (N+1)
result = []

for _ in range(M):
    i, j = map(int, input().split())
    dfsGraph[i].append(j)
    dfsGraph[j].append(i)
    bfsGraph[i].append(j)
    bfsGraph[j].append(i)

for i in range(N+1):
    dfsGraph[i].sort()
    bfsGraph[i].sort()


                
print(*dfs(V))
print(*bfs(V))
