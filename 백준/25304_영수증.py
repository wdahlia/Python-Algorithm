
import sys
sys.stdin = open('25304.txt')

totalPrice = int(input())
purchaseN = int(input())

totalResult = 0
for _ in range(purchaseN):
    price, N = map(int, input().split())
    totalResult += (price * N)

if totalPrice == totalResult:
    print('Yes')
else:
    print('No')