
import re

def solution(new_id):
    answer = ''
    # '.' 는 처음과 끝 사용 X 연속 사용 X
    
    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2.  알파벳 소문자, 숫자, - , _ , .  제외한 모든 문자 제거
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)
    
    # 3. replace 써야됨
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 아이디 처음과 끝에 '.' 위치하면 제거
    
    if new_id == '.':
        new_id = 'a'
    else:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
            
            
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    
    if len(new_id) <= 2:
        w = new_id[-1]
        while len(new_id) < 3:
            new_id += w

    answer = new_id
    
    return answer
