
import sys
sys.stdin = open('5014.txt')

from collections import *

# F, S, G, U, D
# S층에서 G층으로 가기 위해 눌러야하는 버튼 수 최솟값
# 현재있는 층이 S
# 가야되는 층 G
# U는 위로
# D는 아래로
# F는 총 층의 개수
# bfs로 풀면될듯

def bfs(flr):
    queue = deque([flr])
    visited[flr] = True
    
    while queue:
        stair = queue.popleft()
        if stair == g:
            return count[g]
        for i in (stair + u, stair - d):
            if 0 < i <= f and not visited[i]:
                visited[i] = True
                count[i] = count[stair] + 1
                queue.append(i)

    if not count[g]:
        return 'use the stairs'
    

f, s, g, u, d = map(int, input().split())
visited = [False for _ in range(f+1)]
count = [0 for _ in range(f+1)]

print(bfs(s))