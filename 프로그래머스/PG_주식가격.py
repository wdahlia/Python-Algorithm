
def solution(prices):
    # 가격이 떨어지지 않은 기간은 몇초인지를 return
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1

                
        answer.append(cnt)
    
    return answer
