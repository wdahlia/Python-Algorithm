
import sys
sys.stdin = open('1759.txt')

# 최소 한개의 모음, 최소 두 개의 자음으로 구성
# 증가하는 순서로 배열
# 가능성 있는 암호를 모두 구하는 프로그램 작성
# 모음과 자음 수를 만족하게끔 수를 세줘야함

# dfs로 하나를 지정하고 가장깊은곳까지 탐색
# 만약 L 즉, 길이를 만족한다면, 모음, 자음 만족하는지 체크해주어야함
def dfs(n):
    global result

    if n == L:
        cnt = 0

        for char in result:
            if char in 'aeiou':
                cnt += 1

        if cnt >= 1 and len(result) - cnt >= 2:
            print(result)
        return

    for i in range(n, C):
        if not visited[i] and (len(result) == 0 or ord(result[-1]) < ord(alphs[i])):
            visited[i] = True
            result += alphs[i]
            dfs(n+1)
            visited[i] = False
            result = result[:-1]


L, C = map(int, input().split())
alphs = sorted(list(input().split())) # ['a', 'c', 'i', 's', 't', 'w']

result = ''
visited = [False] * len(alphs)
dfs(0)