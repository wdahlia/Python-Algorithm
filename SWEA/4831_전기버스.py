
import sys
sys.stdin = open('4831.txt')

# 중간에 충전기 설치된 정류장
# 최대한 이동할 수 있는 정류장 수 K
# 최소한 몇 번의 충전을 해야 종점에 도착?
# 도착 못하면 0 출력
# 출발지에는 충전기 있지만 충전횟수 포함X

T = int(input())

for i in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    busstop = [0] * (N+1)
    for charge in charger:
        busstop[charge] = 1
    
    past = 0        
    now = past + K  
    cnt = 0

    while now < N:
        if busstop[now] == 1: 
            cnt += 1 
            past = now
            now = now + K 
        
        elif busstop[now] == 0:
            for j in range(1, K+1):
                if busstop[now-j] == 1:
                    cnt += 1
                    past = now - j
                    now = past + K
                    break
            if j == K:
                cnt = 0
                break
    
    print(f'#{i} {cnt}')
    