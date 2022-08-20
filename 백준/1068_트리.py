
import sys
sys.stdin = open('1068.txt')

# 리프 노드의 개수 출력

N = int(input())
nodes = list(map(int, input().split()))
erase_n = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    pass