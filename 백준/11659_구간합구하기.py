
import sys
sys.stdin = open('11659.txt')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())
    