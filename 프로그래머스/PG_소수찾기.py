
import math
from itertools import permutations

n = 10000000

array = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
            

def solution(numbers):
    
    answer = 0
                        
    numbers = list(numbers)
    
    perm = []
    
    for k in range(1, len(numbers) + 1):
        perm += list(permutations(numbers ,k))
    
    for l in range(len(perm)):
        perm[l] = ''.join(perm[l])
        perm[l] = int(perm[l])
    

    perm = list(set(perm))
    
    # [2, 3, 11, 13, 23, 31, 113, 131, 211, 311, 1123, 1213, 1231, 1321, 2113, 2131, 2311, 3121]

    for res in perm:
        if res >= 2 and array[res]:
            print(res, end=' ')
            answer += 1
            
    return answer
    