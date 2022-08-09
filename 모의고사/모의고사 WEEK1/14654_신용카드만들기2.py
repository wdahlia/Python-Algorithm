import sys
sys.stdin = open('신용카드만들기2.txt')

# 두가지 조건 만족해야함
# '-' 제외한 숫자가 16, 카드번호는 3,4,5,6,9로 시작해야함
T = int(input())

for i in range(1, T+1):
    
    case_n = input()

    case_n = case_n.replace('-', '') # replace 함수로 '-'를 제거한다.

    if case_n[0] in '34569' and len(case_n) == 16: # case_n의 첫 인덱스의 숫자가 '34569' 안에 있고 길이가 16이면
        print(f'#{i} 1') # 1 출력
    else: # 하나라도 해당 안되면 0 출력해라
        print(f'#{i} 0')
