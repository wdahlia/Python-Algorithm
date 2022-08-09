
# 접근방법
# absolutes와 signs가 주어짐
# 즉 i가 absolutes 리스트의 len 길이인 range(3) # 0, 1, 2
# i = 0 signs[0]이 True이면, absolutes[0] 역시 양수다
# result값이 absolutes 리스트 요소들의 합이므로

def solution(absolutes, signs):
    
    answer = 0 # 총합을 만들기 위해서 초기값 0 설정
    for i in range(len(absolutes)):
        if signs[i] == True: # True이면, absolutes[i] 역시 양수
            answer += absolutes[i] # True면, 0 + absolutes[0]을 answer에 저장
                                   # 계속 순환하면서 그 값을 answer에 저장
        else: # False이면, absolutes[i]가 음수
            answer -= absolutes[i] # False면, 0 - absolutes[0](즉, 음수를 더해준다)을 answer에 저장
    return answer
