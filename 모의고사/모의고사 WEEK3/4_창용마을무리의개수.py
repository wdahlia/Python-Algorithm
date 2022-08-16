import sys

sys.stdin = open("_창용마을무리의개수.txt")

# DFS

# N = 사람의 수 M = 관계의 수

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = [(list(map(int, input().split()))) for _ in range(M)]
    visited = [False] * (N+1)

    graph = [[] for _ in range(N+1)]
    for idx in range(M):
        graph[arr[idx][1]].append(arr[idx][0])
        graph[arr[idx][0]].append(arr[idx][1])
    
    def dfs(x):
        stack = [x]
        
        while len(stack) != 0:
            next = stack.pop()
            for j in graph[next]:
                if visited[j] != True:
                    visited[j] = True
                    stack.append(j)
                else:
                    continue
            
        
    cnt = 0
    for n in range(1, N+1):
        if visited[n] != True:
            visited[n] = True
            cnt += 1
            dfs(n)

    print(f'#{i} {cnt}')
        
