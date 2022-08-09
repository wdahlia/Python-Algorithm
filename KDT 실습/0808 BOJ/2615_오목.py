
from pprint import pprint

import sys
sys.stdin = open('2615.txt')

# 우 하 우상 우하
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

board = []

for _ in range(N):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

