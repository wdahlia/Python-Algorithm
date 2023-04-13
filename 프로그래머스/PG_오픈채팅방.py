
def solution(record):
    
    # 중복 이름 허용 만약 같은 아이디 닉네임 바뀌면 그 이름으로 대체
    # 딕셔너리..?
    
    dict = {}
    
    answer = []
    
    # if로 Enter, Leave, Change 일 때 다르게

    for notice in record:
        notice = notice.split(' ')
        
        if notice[0] == 'Enter':
            dict[notice[1]] = notice[2]
            answer.append(f'{notice[1]}님이 들어왔습니다.')

        elif notice[0] == 'Leave':
            answer.append(f'{notice[1]}님이 나갔습니다.')
        
        elif notice[0] == 'Change':
            dict[notice[1]] = notice[2]
    
    for i in range(len(answer)):
        answer[i] = answer[i].split('님')
        answer[i][0] = answer[i][0].replace(answer[i][0], dict[answer[i][0]])
        answer[i] = '님'.join(answer[i])
            
    return answer
    