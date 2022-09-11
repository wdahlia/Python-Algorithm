
import sys
sys.stdin = open('1037.txt')

# A가 N의 약수 - N이 A의 배수, A가 1,N 아니여야함

cnt = int(input())

num_li = list(map(int, input().split()))

result = min(num_li) * max(num_li)

print(result)