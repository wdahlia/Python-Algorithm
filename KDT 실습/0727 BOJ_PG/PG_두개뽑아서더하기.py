
def solution(numbers):
    
    # 접근방법
    # 인덱스를 사용해서 두수를 더하는 법
    # 즉 numbers[0]에 있을때 numbers[0] + numbers[1],[2],[3],... 더하고
    # numbers[1]에 있을때 numbers[2],[3],....더하는 식으로 구성
    # 그런 후 중복 있을 수 있으니 set으로 제거하고 list로 변환후 sort 메서드 사용하여 오름차순 정렬
    
    answer = []
    for i in range(len(numbers)):
        for n in range(i+1, len(numbers)):
            sum_n = numbers[i] + numbers[n]
            answer.append(sum_n)
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
