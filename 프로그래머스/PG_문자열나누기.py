
def solution(s):
    # b를 우선 넣고 b a 다른 문자열이고 횟수도 같으니 ba 하나 na 하나 na 하나 즉 3개
    # a b 다른문자열 횟수 같음 ab ra ca da br a
    # aaabbacc ccabba
    answer = 0
    cnt = 0
    
    while s:
        char = s[0]
        for idx in range(len(s)):
            if char == s[idx]:
                cnt += 1
            else:
                cnt -= 1 # 말하자면 같다면 1을 더해주고 다르면 -1 즉 개수가 같은 친구는 빼면 0이되는 것을 활용
            
            if cnt == 0 or idx == len(s) - 1:
                s = s[idx+1:]
                answer += 1
                break
                
        
                
    return answer
    