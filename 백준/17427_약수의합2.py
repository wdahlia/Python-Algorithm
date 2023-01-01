
import sys
sys.stdin = open('17427.txt')


N = int(input())

result = []
for i in range(1, N+1):
    result.append((N//i)*i)
    
print(sum(result))