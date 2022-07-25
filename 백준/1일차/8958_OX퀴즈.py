
T = int(input())

for i in range(T):
    ox_result = input() 
    cnt = 0
    sum_cnt = 0
    for ox in ox_result: # input한 문자열의 인자들을 순환할때
        if ox == 'O': # ox가 'O'와 같다면 cnt에 1을 더해줌
            cnt += 1
            sum_cnt += cnt # sum_cnt에 cnt를 더해줌
        else:
            cnt = 0 
            # 즉 'O'가 연달아 계속 있다면 1씩 계속 증가하며 더해질 것이고
            # 'X'인 경우는 cnt가 초기화됨
    print(sum_cnt)
    # 최종 cnt를 더한 것을 출력
