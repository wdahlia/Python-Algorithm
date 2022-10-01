
def solution(participant, completion):
    
    
    # 선수들 이름 담긴 배열 participant, 완주한 선수 이름 completion
    # 완주하지못한 사람 뽑으쇼
    # completion 길이 participant 길이보다 1 작음 즉, 완주 못한 사람은 1명이 나온다는거
    # 답은 1개다
    # 동명이인 존재
    
    participantList = dict()
    answer = ''
    for people in participant:
        participantList[people] = participantList.get(people, 0)+ 1
        
    
    for person in completion:
        participantList[person] -= 1
        
    for k, v in participantList.items():
        if v >= 1:
            answer = k
            return answer
            