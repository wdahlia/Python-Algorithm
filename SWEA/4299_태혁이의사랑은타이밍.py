
import sys
sys.stdin = open('4299.txt')

# 얼마나 오래 바람 맞았는지 분 단위로 출력
# 소개팅 약속 전에 차였다면 -1

tc = int(input())

for i in range(1, tc+1):
    res = 0
    d, h, m = map(int, input().split())
    res += (d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11)
    if res < 0:
        res = -1

    print(f'#{i} {res}')
   
