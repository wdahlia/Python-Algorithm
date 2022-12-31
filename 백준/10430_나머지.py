
import sys
sys.stdin = open('10430.txt')

A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C)+(B+C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
