from math import factorial

def solution(n, k):
    nums = [i for i in range(1, n+1)]
    k -= 1 
    answer = []
    
    while nums:
        p = k // factorial(n-1)
        answer.append(nums[p])
        del nums[p]
        
        k = k % factorial(n-1)
        n -= 1
    return answer