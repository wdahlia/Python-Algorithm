
# 성격 유형은 16가지가 나올 수 있다 MBTI 생각하면 될 듯
# 선택지 - 매우 비동의, 비동의, 약간 비동의, 모르겠음, 약간 동의, 동의, 매우 동의
# 1 > 7
# 각 지표에서 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라 판단
# 성격 유형 점수가 같다면 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라 판단

# 1 - 라이언(R), 튜브형(T)  - 동일 선상에 있어야됨  - 비동의 관련이면 1[0] 동의 관련 1[1]
# 2 - 콘형(C), 프로도형(F)
# 3 - 제이지형(J), 무지형(M)
# 4 - 어피치형(A), 네오형(N)

# 지표 번호 순서대로 return


survey = ['AN', 'CF', 'MJ', 'RT', 'NA']
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    
    dict = {
    'R' : 0,
    'T' : 0,
    'C' : 0,
    'F' : 0,
    'J' : 0,
    'M' : 0,
    'A' : 0,
    'N' : 0,
    }

    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        else:
            if choices[i] < 4:
                dict[survey[i][0]] += 4 - choices[i]  
            # 'AN' 일때 'A' choices[i] == 3이라면 약간 비동의이다. 즉, 1이므로 4에서 choices[i]값 뺀것과 같음
            elif choices[i] > 4:
                dict[survey[i][1]] += choices[i] - 4 
            # 'AN' 일때 'N' choices[i] == 6이라면 동의이다. 즉, 2이므로 choices[i]값에서 4 뺀것과 같음
                
    key_list = list(dict.keys())

    result = ''
    for j in range(0, len(dict), 2):
        if dict.get(key_list[j]) >= dict.get(key_list[j+1]):
            result += key_list[j]
        elif dict.get(key_list[j]) < dict.get(key_list[j+1]):
            result += key_list[j+1]

    return result
