
import sys
sys.stdin = open('2644.txt')

from pprint import pprint

# 촌수 계산
# 부모 - 자식 : 1촌
# 아버지 - 할아버지 : 1촌
# 나 - 할아버지 : 2촌
# 나 - 아버지 형제들 : 3촌
# 촌수 없는 경우 -1

# 전체 사람의 수
N = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
A, B = map(int, input().split())

relation_n = int(input())


family = [[] for _ in range(N+1)]

par = []

for _ in range(relation_n):
    parent_n, child_n = map(int, input().split())
    family[parent_n].append(child_n)
    family[child_n].append(parent_n)

print(family)


def dfs(A, B): # dfs 함수 정의

    need_visited = [False] * (N+1)
    stack = [(A, 0)]
    need_visited[A] = True 
    # 시작 값을 안넣어주기 위함  
    # 밑의 if not need_visited[people] 즉, False이면 append 해야하므로

    result = -1

    while len(stack) != 0:
        current, cnt = stack.pop()
        print(current, cnt)
        
        if current == B:
            result = cnt
            break

        f_graph = family[current]

        for people in f_graph:
            if not need_visited[people]:
                stack.append((people, cnt + 1))
                print(stack)
                need_visited[people] = True
    print(need_visited)
    return result

print(dfs(A, B))


