
import sys
sys.stdin = open('신용카드만들기1.txt')

T = int(input())

for i in range(1, T+1):

    case_n = list(map(int, input().split()))

    # 1,2번 조건을 만족하기 위한 식을 세운다
    # 1. 매 홀수자리는 숫자마다 2를 곱해서 더하고
    # 2. 매 짝수자리는 그대로 더해준다
    # 인덱스는 0부터 읽지만 사실상 숫자 읽을땐 첫번째 숫자 두번째 숫자 이렇게 읽기 때문에
    sum_case = 0 
    for idx in range(15):
    # for문에서 case_n의 len길이만큼 range를 돌려주는걸 idx로 잡아줌 사실 len(case_n)으로 range 안잡고 
    # 주어진 테스트 케이스 숫자들이 동일하므로 15로 한다.
    # for idx in range(len(case_n)):
    # ^ 이전코드 : 
        if (idx + 1) % 2 == 1: # idx+1 해준 값을 2로 나눴을 때 나머지가 1이라면 홀수다
            sum_case += (case_n[idx] * 2) # 그 인덱스에 2를 곱해서 sum_case에 더해준다
        elif (idx + 1) % 2 == 0: # 나머지가 0이라면 짝수
            sum_case += case_n[idx] # 그대로 그냥 sum_case에 더해준다
    
    # 그리고 그 합한 값이 10으로 나누어 떨어졌을때는 0 출력
    # 나누어 떨어지지 않는다면 끝자리가 0이 되게끔 만들어 주어야 함
    if sum_case % 10 == 0: 
        print(f'#{i} 0')
    else:
        remainder_n = sum_case % 10 # 10으로 나눈 나머지를 remainder_n에 저장
        result = 10 - remainder_n # 10에서 remainder_n 한 값이 result가 된다
        print(f'#{i} {result}')
