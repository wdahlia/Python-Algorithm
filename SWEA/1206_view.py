
import sys
sys.stdin = open('1206.txt')

# 빌딩의 높이 0 에서 255까지
# 맨 왼쪽, 맨 오른쪽 두칸은 항상 높이가 0
# 조망권의 확보는 각각 좌우로 2칸 이상의 공백이 존재해야함

T = 10

dx = [-2, -1, 1, 2]
for i in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    result = [0] * N
    
    for idx in range(N):
        mx = 0
        for k in range(4):
            nx = idx + dx[k]
            if -1 < nx < N:
                if height[nx] > mx:
                    mx = height[nx]

        if height[idx] > mx:
            result[idx] = height[idx] - mx

    print(f'#{i} {sum(result)}')
