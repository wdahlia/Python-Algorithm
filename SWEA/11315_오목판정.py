
T = int(input())

# 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 판정하는 프로그램
# 있으면 yes, 아니면 no

dx = [0, 1, 1, 1] # 우 하 우하 좌하
dy = [1, 0, 1, -1]


def Omok(matrix):
  for i in range(N):
    for j in range(N):
      if matrix[i][j] == 'o':
        for idx in range(4):
          cnt = 1
          nx = i + dx[idx]
          ny = j + dy[idx]
          
          while 1:
            if -1 < nx < N and -1 < ny < N and matrix[nx][ny] == 'o':
              nx, ny = nx + dx[idx], ny + dy[idx]
              cnt += 1
            else:
              break

          if cnt >= 5:
            return 'YES'

  return 'NO'

for tc in range(1, T+1):
  answer = 0
  N = int(input())
  matrix = [list(input()) for _ in range(N)]

  print(f'#{tc} {Omok(matrix)}')
 