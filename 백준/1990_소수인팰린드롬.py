
import sys
sys.stdin = open('1990.txt')

# 팰린드롬 앞으로 읽으나 뒤로 읽으나 같은 수를 의미

import math

# 에라토스테네스의 체를 이용하여 소수들을 우선 메모제이션
# 전부다 팰린드롬수를 찍어봤을떄 마지막 팰린드롬수가 9989899 즉, 백만 까지밖에 없음
# pypy로만 통과

a, b = map(int, input().split())

if b > 10000000:
    b = 10000000

array = [True for _ in range(10000001)]


for i in range(2, 10001):
    if array[i]:
        j = 2
        while i * j <= 10000000:
            array[i * j] = False
            j += 1

for k in range(a, b+1):
    if array[k]:
        k = str(k)
        if len(k) == 1:
            print(k)
        else:
            if k == k[::-1]:
                print(k)

print(-1)