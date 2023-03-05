
def solution(numbers, target):
    # bfs로 문제 풀이
    # 음수, 양수로 나누어서 풀어야됨
    answer = 0
    array = [0]

    for n in numbers:
        result = []
        for i in array:
            result.append(i + n)
            result.append(i - n)
        array = result

    answer = result.count(target)
    
    return answer
    