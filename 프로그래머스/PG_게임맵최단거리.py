
from collections import deque

def solution(maps):
    answer = 0
    
      
    dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    
    rows = len(maps)
    columns = len(maps[0])
    
    
    def bfs(i, j):
        
        queue = deque()
        queue.append((i, j))
        
        
        while queue:
            r, c = queue.popleft()
            
            for idx in range(4):
                nx = r + dx[idx]
                ny = c + dy[idx]
                if -1 < nx < rows and -1 < ny < columns and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[r][c] + 1
                    queue.append((nx, ny))
            
        return maps[rows-1][columns-1]
        
    answer = bfs(0, 0)
    
    if answer == 1:
        answer = -1
            
    return answer
    