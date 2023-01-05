
import sys
sys.stdin = open('1676.txt')

N = int(input())

result = 1
for i in range(N, 0, -1):
    result *= i

zero_cnt = 0
while (result % 10 == 0):
    if result % 10 == 0:
        result //= 10
        zero_cnt += 1

print(zero_cnt)