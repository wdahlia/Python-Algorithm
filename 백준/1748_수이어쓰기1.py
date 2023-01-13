
import sys
sys.stdin = open('1748.txt')

# 새로운 수의 자릿수를 구하는 프로그램을 작성
# N까지의 수를 이어서 쓰는 경우의 그 수의 길이
# N은 1억개의 수도 나올수 있음

N = int(input())

length = len(str(N))

cnt = 0
while length:
    cnt += (N - (10**(length-1)) + 1)
    length -= 1

print(cnt)