
import sys
sys.stdin = open('9613.txt')

import math
# 모든 쌍의 GCD의 합을 구하는 프로그램 작성
# 최대공약수를 구하는 내장 함수 사용
# 두가지 방법 존재

# 1

T = int(input())

def gcd(x, y):
    while y != 0:
        num = x % y
        x, y = y, num
    return abs(x)
   

for _ in range(T):
    array = list(map(int, input().split()))
    n = array[0]

    result = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            result += gcd(array[i], array[j])


    print(result)
    
# 2

T = int(input())

for _ in range(T):
    array = list(map(int, input().split()))
    n = array[0]

    result = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            result += math.gcd(array[i], array[j])


    print(result)
    