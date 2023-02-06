
import sys
sys.stdin = open('17298.txt')

N = int(input())
array = list(map(int, input().split()))
result = [-1] * N
stack = []
for i in range(N):
    while stack:
        if array[stack[-1]] < array[i]:
            res = stack.pop()
            result[res] = array[i]
        else:
            break
        
    stack.append(i)


print(*result)