
import sys
sys.stdin = open('2477.txt')

melon = int(input())

max_ns , max_we = 0, 0
nswe = []
for _ in range(6):
    d, length = map(int, input().split())

    if d == 4 or d == 3:
        nswe.append((d, length))
        if length > max_ns:
            max_ns = length

    if d == 2 or d == 1:
        nswe.append((d, length))
        if length > max_we:
            max_we = length

for idx in range(6):
    if nswe[idx][0] == 1 or nswe[idx][0] == 2:
        if max_we == nswe[idx][1]:
            small_w = nswe[idx+2][1]

    if nswe[idx][0] == 3 or nswe[idx][0] == 4:
        if max_ns == nswe[idx][1]:
            small_h = nswe[idx+4][1]




max_res = max_ns * max_we
min_res = small_w * small_h

print(((max_res) - (min_res)) * melon)
