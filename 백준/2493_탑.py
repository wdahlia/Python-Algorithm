
import sys
sys.stdin = open('2493.txt')

N = int(input())
tower = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(N):
    while stack:
        if tower[i] <= stack[-1][0]:
            result[i] = stack[-1][1]
            stack.append((tower[i], i+1))
            break
        
        else:
            stack.pop()

        if not stack:
            stack.append((tower[i], i+1))
            break
    else:
        stack.append((tower[i], i+1))

print(*result)