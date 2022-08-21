
import sys
sys.stdin = open('4963.txt')

# 땅은 1 바다는 0
# 두 정사각형이 같은 섬에 있다. 한 정사각형에서 다른 정사각형으로 걸어서
# 나갈 수 있는 경로가 있어야 됨 그렇다면 하나임.
#

# 너비 w 높이 h

import sys

while True:
    w, h = map(int, sys.stdin.readline().split())

    if (w, h) == (0, 0):
        break
    else:
        island_map = [list(map(int, input().split())) for _ in range(h)]

