
def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        cnt = 0
        j = i
        while j:
            if i % j == 0:
                cnt += 1
            j -= 1
        
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
    