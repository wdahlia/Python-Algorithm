
import sys
sys.stdin = open('1978.txt')

N = int(input())

def is_prime_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False # 소수가 아니다

    return True # 소수이다

array = list(map(int, input().split()))

cnt = 0
for num in array:
    if num > 1 and is_prime_num(num):
        cnt += 1

print(cnt)
