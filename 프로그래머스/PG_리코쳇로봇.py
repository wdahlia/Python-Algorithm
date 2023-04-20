from collections import deque

def solution(board):
    
    # 장애물이나 맨끝에 부딪힐때까지 미끄러져 이동하는 것을 한번의 이동이라고 침
    # R 로봇의 처음 위치
    # 최소 이동해서 G까지 가게끔 bfs
    N = len(board)
    M = len(board[0])
    queue = deque()
    
    dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    
    visited = [[0] * M for _ in range(N)]
    
    switch = False
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                queue.append((i, j, 1))
                switch = True
        if switch:
            break

    while queue:
        r, c, cnt = queue.popleft()

        if board[r][c] == 'G':
            return cnt - 1

        for idx in range(4):

            nx, ny = r, c

            
            while 0 <= nx + dx[idx] < N and 0 <= ny + dy[idx] < M and board[nx + dx[idx]][ny + dy[idx]] != 'D':
                
                nx += dx[idx]
                ny += dy[idx]
                

            if visited[nx][ny] == 0 or visited[nx][ny] >= cnt + 1:
                visited[nx][ny] = cnt + 1
                queue.append((nx, ny, cnt+1))       

    return -1
    