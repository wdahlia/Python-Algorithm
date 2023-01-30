
def solution(t, p):
    # 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수 return
    
    answer = 0
    
    length = len(p)
    cnt = length
    
    for i in range(len(t) - (length-1)):
        char = ''
        for j in range(cnt):
            char += t[i+j]
        
        if int(char) <= int(p):
            answer += 1
            
    return answer
    