
import sys
sys.stdin = open('17103.txt')

T = int(input())
array = [True for _ in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        j = 2
        while i * j <= 1000000:
            array[i * j] = False
            j += 1

for _ in range(T):
    n = int(input())
    cnt = 0
    for k in range(2, (n//2) + 1):
        if array[k] and array[n-k]:
            cnt += 1
    print(cnt)