
def solution(s):
    # 딕셔너리로 구현
    answer = []
    alph_dict = {}
    
    for i in range(len(s)):
        if s[i] not in alph_dict:
            answer.append(-1)
            alph_dict[s[i]] = i
        else:
            nearby_num = i - alph_dict.get(s[i])
            answer.append(nearby_num)
            alph_dict[s[i]] = i
            