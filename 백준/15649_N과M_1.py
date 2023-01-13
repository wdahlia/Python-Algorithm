
import sys
sys.stdin = open('15649.txt')

# N,M이 주어졌을 때, 길이가 M인 수열을 모두 구하기


def permutation(N, M):

    if len(array) == M:
        print(*array)

    for i in range(1, N+1):
        if not visited[i]:
            array.append(i)
            visited[i] = True
            permutation(N, M)
            visited[i] = False
            array.pop()

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
array = []

permutation(N, M)