
import sys
sys.stdin = open('1527.txt')

input = sys.stdin.readline

def dfs(x):
    global cnt

    if len(str(x)) > lenB:
        return
    if lenA <= len(str(x)) <= lenB:
        if A <= x <= B:
            cnt += 1

    for i in 4, 7:
        number = 10 * x + i
        dfs(number)



A, B = map(int, input().split())
lenA = len(str(A))
lenB = len(str(B))
cnt = 0
dfs(4)
dfs(7)

print(cnt)
