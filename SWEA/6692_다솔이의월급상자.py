
import sys
sys.stdin = open('6692.txt')

# 월급을 상자에 담아주기로 함
# p의 확률로 x 만원이 들어있음
# 월급의 평균은?

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0
    for _ in range(N):
        px = input().split()
        p = float(px[0])
        x = int(px[1])
        result += p * x

    print(f'#{tc} {result:.6f}')
    