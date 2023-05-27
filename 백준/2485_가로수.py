
import sys
sys.stdin = open('2485.txt')

from math import gcd

# gcd 내장 함수사용
# 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램
# 기존의 나무 사이에만 심을 수 있음
# 최대공약수 찾으면 될거같기도

N = int(input())

tree = []
for _ in range(N):
    tree.append(int(input()))

arr = []
for i in range(N-1):
    arr.append((tree[i+1] - tree[i]))

g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])

res = 0
for num in arr:
    res += (num // g) - 1

print(res)