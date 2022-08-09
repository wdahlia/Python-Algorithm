
# input
'''
2
5 30 25 76 23 78
6 25 50 70 99 70 90
'''
# output
'''
Class 1
Max 78, Min 23, Largest gap 46
Class 2
Max 99, Min 25, Largest gap 25
'''
import sys
sys.stdin = open('5800.txt')

# Class {test_case}
# Max , Min, Largest gap 뒤에 각 점수 출력

T = int(input())

# 쉽게 푸는 방법 # 76ms 
for t in range(1, T+1): # 출력값 Class 뒤에 숫자 붙이기 위함
    li = list(map(int, input().split()))
    N = li[0] # n의 개수는 li[0]
    score = li[1:] # 점수 리스트

    max_score = max(score) # 최대값
    min_score = min(score) # 최소값

    result = sorted(score, reverse=True) # 내림차순으로 정렬
    empty = []
    for i in range(len(score)-1): # len(score)만 할 경우 인덱스를 벗어남 i+1이랑 빼줄것이여서
        r = result[i] - result[i+1] # 인접한 두 점수를 빼서 
        empty.append(r) # 그 값을 empty에 append 해준다
    gap = max(empty) # 최대값을 구해준다

    print(f'Class {t}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}') # 출력해준다

    
# 쉽게 푸는 방법 외 다른 방법으로 짜 봄 # 84ms
for t in range(1, T+1): 
    li = list(map(int, input().split()))
    N = li[0]
    score = li[1:]
    # 0 <= 시험성적 <= 100
    max_score = 0 # 큰 값들을 갱신하기 위해서는 제일 작은 0으로 설정
    min_score = 100 # 작은 값을 비교하기 위해 제일 큰 값으로 설정
    for idx in range(N): # 순회
        if score[idx] > max_score: # 만약 score가 max_score보다 크면
            max_score = score[idx] # max_score 갱신
            if max_score < min_score: 
                # 근데 만약에 max_score이 min_score보다 작은경우 즉 리스트의 0번째 인덱스가 최소값일 경우
                # max_score값에 갱신되니까
                min_score = max_score # min_score에 할당해줘
        else: # score가 max_score보다 작은 경우
            if score[idx] < min_score: # min_score보다 작으면
                min_score = score[idx] # min_score에 할당

    result = sorted(score, reverse=True)
    empty = []
    for i in range(len(score)-1):
        r = result[i] - result[i+1]
        empty.append(r)
    gap = max(empty)

    print(f'Class {t}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')
