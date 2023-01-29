from collections import deque
import sys
sys.setrecursionlimit(10**6)

# 지도의 'X'는 바다, 숫자는 무인도
# 상 하 좌 우 해당 무인도에서 최대 며칠 동안 머물 수 있는가
# 최대 몇일? 배열에 오름차순으로 담아 return
# 지낼 수 있는 것이 없다면 -1을 배열에 담아 return
# dfs, bfs로 풀 수 있을 듯

def solution(maps):
    
    def bfs(x, y, days_cnt):
        
        queue = deque([(x, y)])
        while queue:
            r, c = queue.popleft()
            for idx in range(4):
                nx = r + dx[idx]
                ny = c + dy[idx]
                if -1 < nx < N and -1 < ny < M:
                    if matrix[nx][ny] != 'X' and not visited[nx][ny]:
                        days_cnt += int(matrix[nx][ny])
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        return days_cnt
        
    answer = []

    N = len(maps)
    M = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    matrix = [list(elements) for elements in maps]
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            days_cnt = 0
            if not visited[i][j] and matrix[i][j] != 'X':
                days_cnt += int(matrix[i][j])
                visited[i][j] = True
                answer.append(bfs(i, j, days_cnt))
                
    
    if len(set(answer)) == 0:
        return [-1]
    
    else:
        return sorted(answer)
    