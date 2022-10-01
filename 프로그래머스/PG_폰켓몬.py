def solution(nums):
    
    # n마리 중 절반 가져가도 좋다~
    # 최대 가질 수 있는 종류의 수
    # 최대한 많은 종류의 폰켓몬 포함 n/2 선택
    # 종류는 항상 짝수로 주어짐
    
    ponkemon = dict()
    for num in nums:
        ponkemon[num] = ponkemon.get(num, 0) + 1
        
    maxnumber =  len(nums) / 2
    lenDict = len(ponkemon)
    
    result = 0
    if maxnumber > lenDict:
        result = lenDict
    else:
        result = maxnumber
        
    return result