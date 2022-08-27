
import sys
sys.stdin = open('1859.txt')

# 연속된 N일 동안의 물건의 매매가 예측해서 알고 있다
# 하루에 최대 1만큼 구입할 수 있다
# 판매는 얼마든지 가능
# 1 2 3 마지막 날에 팔면 3의 이익 낼수 ㅇ
# 즉, max값이 첫째날에 있다면 > 0을 뱉어내자 (안 사는게 이득)
# max값이 있는 인덱스에서 팔아야되는데 아...max를 구하지말고 인덱스 돌면서 갱신
# 1씩 사다가 max나오면 팔자..

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
 
    lst = list(map(int, input().split()))[::-1]
    ans = mx = 0
    for n in lst:
        if mx < n:
            mx = n
        else:
            ans += (mx-n)
 
    print(f'#{test_case} {ans}')


T = int(input())

for i in range(1, T+1):

    N = int(input())
    price = list(map(int, input().split()))
    end = N-1
    max_ = max(price)
    start = sum_ = result = n = 0

    while start <= end:
        if price[0] == max_:
            result = 0
            break
        else:
            if price[start] < max_:
                sum_ += price[start]
                price[start] = 0
                start += 1
                n += 1
            elif price[start] == max_:
                result += ((price[start] * n) - sum_)
                price[start] = sum_ = n = 0
                start += 1
                max_ = max(price)
                if start == end:
                    break

    print(f'#{i} {result}')
                