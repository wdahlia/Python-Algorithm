import sys

sys.stdin = open("_조교의성적매기기.txt")


T = int(input())


for t in range(1, T+1):
    
    n, k = list(map(int, input().split()))
    gp = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-'] # 각 점수 리스트를 구성해준다

    
    score_list = []
    for i in range(n):
        mid, final, hw = list(map(int, input().split())) # 중간고사 # 기말고사 # 과제를 각각 할당해준다
        sum_score = (mid * 0.35) + (final * 0.45) + (hw * 0.2) # 각 점수의 비율에 따라 곱해준 다음 sum_score에 할당
        score_list.append([sum_score, i+1]) # sum_score와 인덱스는 0부터 시작하므로 순위를 나타내려면 인덱스에 +1한 값을 리스트로 묶어서 score_list에 append

    score_li = sorted(score_list, reverse=True) # 내림차순으로 sorted한 값을 score_li에 저장해준다

    n_gp = n // 10 # gp의 요소마다 할당되는 인원 수

    for i in range(n):
        if k == score_li[i][1]: # 만약 내가 알고자 하는 k값이 score_li의 [i]인덱스의 1번째 인덱스와 일치하면
            idx = i // n_gp # 그 인덱스 값은 i를 n_gp 값으로 나눈 몫이다 만약, n_gp가 3이라면 3명까지는(i = 0,1,2) 인덱스는 계속 0 즉, gp[idx] A+가 된다
            print(f'#{t} {gp[idx]}')

    
        