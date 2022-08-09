
# input
'''
10 500
93 181 245 214 315 36 185 138 216 295
'''
# output 497

import sys
sys.stdin = open('2798.txt')

n, sum_ = list(map(int, input().split()))
numbers = list(map(int, input().split()))

def blackjack(n, sum_, numbers): # 함수 정의해준다

    max_sum = 0 # max_sum의 초기값 설정

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                sum_num = numbers[i] + numbers[j] + numbers[k]
            
                if max_sum < sum_num < sum_: # sum_num이 sum_초과하면 안되므로 조건 추가
                    max_sum = sum_num

                if sum_num == sum_: # 만약 sum_num == sum_ 이라면
                    return sum_num # return하고 끝 (더 돌릴 필요도 없음)

    return max_sum

result = blackjack(n, sum_, numbers)
print(result)
