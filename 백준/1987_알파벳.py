
import sys
sys.stdin = open('1987.txt')

# import sys
# input = sys.stdin.readline

# # DFS 문제
# # 반복되는 알파벳이 있다면 지날 수 없음
# # 델타 탐색도 해야함
# def dfs(x, y):
#     global alph
#     global result

#     if len(alph) > result:
#         result = len(alph)

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1] # 상하좌우

#     for idx in range(4):
#         nx = x + dx[idx]
#         ny = y + dy[idx]
#         if 0 <= nx < i and 0 <= ny < j:
#             if matrix[nx][ny] not in alph:
#                 alph.add(matrix[nx][ny])
#                 print(alph)
#                 dfs(nx, ny)
#                 alph.remove(matrix[nx][ny])
#                 print(alph)
    
#     return result



# i, j = map(int, input().split())
# matrix = [list(input()) for _ in range(i)]

# result = 0
# x, y = [0, 0]
# alph = set()
# alph.add(matrix[x][y])

# print(dfs(x, y))

def dfs(x, y):
    global alph
    global result

    if len(alph) > result:
        result = len(alph)
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < i and 0 <= ny < j:
            if matrix[nx][ny] not in alph:
                alph.add(matrix[nx][ny])
                dfs(nx, ny)
                alph.remove(matrix[nx][ny])
            else:
                continue

    return result



i, j = map(int, input().split())
matrix = [list(input()) for _ in range(i)]

result = 0
x, y = [0, 0]
alph = set()
alph.add(matrix[x][y])


print(dfs(x, y))