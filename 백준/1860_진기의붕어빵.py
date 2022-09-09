
import sys
sys.stdin = open('1860.txt')

#30 Impossible

# 0초 부터 붕어빵 만들어서 M초의 시간 들이면 K개의 붕어빵 만들 수 있다


T = int(input())

for i in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()

    
    result = 'Possible'
    for idx in range(N):
        rest = K * (arrive[idx] // M) - (idx + 1)
        if rest < 0:
            result = 'Impossible'
            break
            
    print(f'#{i} {result}')