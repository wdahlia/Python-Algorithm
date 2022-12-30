def solution(k, score):
    # k의 값이 곧 등수이다, 그 등수에서 k번째 까지 슬라이싱 한 후 min값을 찾기
    # 그 값을 answer에 집어 넣기
    array = []
    answer = []
    for i in score:
        array.append(i)
        array.sort(reverse=True)
        array = array[:k]
        answer.append(array[-1])
    return answer