
import sys
sys.stdin = open('5209.txt')

T = int(input())



# 백트래킹인거같은데에에에

# 93 4 65 31 66 93 + 12 
# 63 12 60 60 84
# 87 57 44 35 20
# 12 9 40 12 40
# 60 21 3 49 54

def dfs(idx, total):
    global max_num

    if idx == N:
        if max_num > total:
            max_num = total
        return

    if max_num <= total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, total + cost_matrix[idx][i])
            visited[i] = 0

    return max_num
    

for tc in range(1, T+1):
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    max_num = 1485
    print(f'#{tc} {dfs(0, 0)}')