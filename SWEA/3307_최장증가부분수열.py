
import sys
sys.stdin = open('3307.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    dp = [1] * N
    dp[0] = 1 # 맨 처음값은 1로 초기화

    for i in range(1, N):
        maxNum = 0
        for j in range(i-1, -1, -1):
            if array[i] >= array[j]: # 해당 인덱스보다 작은 인덱스들을 돌면서 숫자 비교한이후 i가 크다면
                if maxNum < dp[j]:
                    maxNum = dp[j]
            
        dp[i] = maxNum + 1    

            
    print(f'#{tc} {max(dp)}')
    