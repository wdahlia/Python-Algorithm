
import sys
sys.stdin = open('11725.txt')

import sys
sys.setrecursionlimit(10**6)

def dfs(idx):
    for i in li[idx]:
        if parent[i] == 0:
            parent[i] = idx     # 부모를 넣어준다
            dfs(i)

N = int(input())
li = [[] for _ in range(N+1)]
parent = [0] * (N+1) 

for _ in range(N-1):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

dfs(1)                      # 1번 부터 시작

for j in range(2, N+1):
    print(parent[j])