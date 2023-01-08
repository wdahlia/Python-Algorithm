
import sys
sys.stdin = open('2004.txt')

# 조합의 공식 기억 nCk n! / k! * (n-k)!
# m <= n
input = sys.stdin.readline

N, M = map(int, input().split())

def count(num, d):
    cnt = 0
    while num:
        cnt += num // d
        num //= d
    return cnt

cnt_two = count(N, 2) - count(M, 2) - count(N-M, 2)
cnt_five = count(N, 5) - count(M, 5) - count(N-M, 5)

print(min(cnt_two, cnt_five))