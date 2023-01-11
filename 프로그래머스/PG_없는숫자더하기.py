
def solution(numbers):
    answer = 45
    for i in numbers:
        answer -= i
    return answer