
who_is_winner = []
for p in range(1, 6): # 우선 참가자는 5명으로 고정이라고 했다, 즉, 불변 값!
                      # 따라서 range를 1, 6까지 잡은 다음
    score_list = sum(map(int, input().split())) # score_list에 입력받은 값을 int로 형변환해서 sum한 값을 할당
    who_is_winner.append([p, score_list]) # who_is_winner라는 []리스트에 리스트를 추가한다.

win = who_is_winner[0][1] # max를 쓰기 싫어서 비교하는 방법 사용
i = who_is_winner[0][0] # 인덱스 첫번쨰 값의 0번째 인덱스와 1번쨰 인덱스를 각각 변수에 할당
for winner in who_is_winner: # 리스트를 순환할 때
    if winner[1] > win: # 첫번째 인덱스의 [1]인덱스 값이 win보다 크다면
        win = winner[1] # winner[1] 값을 win에 할당 그러면서 제일 큰값을 찾아 가는 것
        i = winner[0] # 얘도 마찬가지

print(f'{i} {win}')
