
import sys
sys.stdin = open('18258.txt')

import sys
input = sys.stdin.readline
from collections import deque

# push X =- 정수 X를 큐에 넣는다
# pop 큐에서 가장 앞에있는 정수 빼고 그수 출력
# 정수 없으면 -1 출력
# size 큐에 들어있는 정수의 개수
# empty 큐 비어있음 1 아니면 0
# front 큐 가장 앞에 있는 정수 출력 큐에 정수 X -1
# back 큐 가장 뒤에 있는 정수 출력 정수 X -1 출력

N = int(input())
queue = deque()

for _ in range(N):
    list_ = input().split()
    command = list_[0]
    if command == 'push':
        queue.append(list_[1])

    elif command == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif command == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif command == 'pop':
        if not queue:
            print(-1)
        else:
            number = queue.popleft()
            print(number)
