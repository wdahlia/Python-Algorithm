
# input
'''
1
20000
3
1 500 500
5 3000 15000
5 5000 25000
'''
# output 
'''
13200
50000
'''
import sys
sys.stdin = open('9325.txt')

# Test case 개수
T = int(input())

for _ in range(T):
    result = 0
    price = int(input()) # 자동차 가격
    option_n = int(input()) # 옵션의 개수
    for _ in range(option_n):
        n, n_price = list(map(int, input().split())) # 입력값 받아주고
        result += (n * n_price) # result에 옵션 개수와 옵션 가격 더해준다음
    result += price # 반복문 끝나면 price 더해줌
    print(result) # 그 결과 출력

    # 원래 생각했던 로직은 if else문 사용해서 option_n == 0 인걸 고려하려 했지만
    # 생각해보니 option이 0이면 그대로 result(0) += price 출력할 것 같아서
    # 위 코드 처럼 작성
