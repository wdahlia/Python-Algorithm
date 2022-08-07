import sys
sys.stdin = open('2161_카드1.txt')

from collections import deque

N = int(input())

num_list = []
for _ in range(1, N+1):
    num_list.append(_)

n_list = deque(num_list)

result_list = []
while len(n_list) != 1:
    result_list.append(n_list.popleft())
    n_list.append(n_list.popleft())

print(*result_list, *list(n_list))

        
