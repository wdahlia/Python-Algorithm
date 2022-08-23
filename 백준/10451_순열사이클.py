
import sys
sys.stdin = open('10451.txt')

def dfs(number):
    stack = [number]

    while len(stack) != 0:
        num = stack.pop()
        graph_1 = graph[num]
        for graph_n in graph_1:
            if not visited[graph_n]:
                stack.append(graph_n)
                visited[graph_n] = True

tc = int(input())                       
for _ in range(tc):
        
    N = int(input())

    arr = list(map(int, input().split()))
    visited = [False] * (N+1)
    graph = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        if i == arr[i-1]:
            graph[i].append(arr[i-1])
        else:
            graph[i].append(arr[i-1])
            graph[arr[i-1]].append(i)
    
    result = 0
    for i in range(1, N+1):
        if visited[i] != True:
            visited[i] = True
            dfs(i)
            result += 1

    print(result)

def dfs(number):
    visited[number] = True
    next = arr[number]
    if not visited[next]:
        dfs(next)

tc = int(input())    
for _ in range(tc):

    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    result = 0

    for idx in range(1, N+1):
        if visited[idx] == False:
            dfs(idx)
            result += 1

    print(result)
