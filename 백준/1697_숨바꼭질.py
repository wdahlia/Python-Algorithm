
import sys
sys.stdin = open('1697.txt')

from collections import deque

# N에서 부터 K까지
# 걷기 - 1초마다 X-1 X+1로 이동
# 순간이동 - 1초후에 2X의 위치로 이동
# 가장 빠른 시간 몇 초 후인가
# 우선 그래프를 만들어서, N부터 K+1의 범위내에서 X-1 X+1 2X를 만족한다면 그래프에 그 노드의 값을 채워넣어주기
# visited를 만들고 그다음은 bfs로 해서 탐색해서 cnt 하면 될거같음


def bfs():
    queue = deque([N])

    while 1:
        num = queue.popleft()

        if num == K:
            print(array[num])
            break
        
        else:
            for i in ( num-1, num+1, 2*num ):
                if 0 <= i <= limit and not array[i]:
                    array[i] = array[num] + 1
                    queue.append(i)
    

N, K = map(int, input().split())
limit = 10 ** 5
array = [0] * (limit + 1)

bfs()