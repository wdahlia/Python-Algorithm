
from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []
    while len(arr) != 0:
        number = arr.popleft()
        if not answer:
            answer.append(number)
        else:
            if number != answer[-1]:
                answer.append(number)
            
    return answer
