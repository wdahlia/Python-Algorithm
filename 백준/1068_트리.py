
import sys
sys.stdin = open('1068.txt')

# 리프 노드의 개수 출력
input = sys.stdin.readline

def dfs(num, array):
    array[num] = -2
    for i in range(len(array)):
        if num == array[i]:
            dfs(i, array)

n = int(input())
array = list(map(int, input().split()))
k = int(input())
cnt = 0

dfs(k, array)

for i in range(len(array)):
    if array[i] != -2 and i not in array:
        cnt += 1
print(cnt)
