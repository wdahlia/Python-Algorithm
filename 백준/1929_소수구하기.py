
import sys
sys.stdin = open('1929.txt')

import math

# 에라토스테네스의 체

M, N = map(int, input().split())
array = [True for _ in range(1000001)]

for i in range(2, int(math.sqrt(1000000))+1):
    j = 2
    while i * j <= N:
        array[i*j] = False
        j += 1

for num in range(M, N+1):
    if num != 1:
        if array[num]:
            print(num)
