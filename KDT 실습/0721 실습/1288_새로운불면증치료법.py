
import sys
sys.stdin = open('1288.txt', 'r')

# input : 1692 ; output : 5076
# N = 1692 1, 6, 9, 2 
# 2N = 3384 3, 8, 4
# 3N = 5076 5, 0, 7 
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 숫자를 모두 보았을 때 종료
# 즉, 출력해야할 값 5076

T = int(input())
for i in range(1, T+1): # #1, #2 출력하기 위함
    num = int(input()) # 입력 값을 받아주고
    num1 = num # num1에 원본 num을 할당해준다
    sleep_list = [] # 빈 리스트를 만들어주고
    while len(sleep_list) < 10: # sleep_list의 길이가 10보다 작을 때
        for n in str(num): # 입력 값을 str 변환한 값 즉, 269면 2 6 9
            if n not in sleep_list: # sleep_list에 없다면
                sleep_list.append(n) # 넣어주세요
        if len(sleep_list) == 10: # 위의 for문이 끝나고 sleep_list가 10이면
            break # 멈춰라
        num += num1 # 다음 순환 전에 num에 원본 더해준다 2k, 3k의 효과
    print(f'#{i} {num}')
