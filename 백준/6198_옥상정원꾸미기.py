
import sys
sys.stdin = open('6198.txt')

# 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있다면 그 다음에 있는 모든 빌딩의 옥상은 보지 못함

N = int(input())
heightArray = [int(input()) for _ in range(N)]
stack = []

cnt = 0
for i in range(N):
    while stack and stack[-1] <= heightArray[i]:
        stack.pop()
    stack.append(heightArray[i])

    cnt += len(stack) - 1

print(cnt)
