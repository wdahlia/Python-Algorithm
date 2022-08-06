import sys

sys.stdin = open("_파리퇴치.txt")

# 처음에는 n-m-1 인덱스 내에서 도는 건줄 알았는데 답이 안나와서
# n-m+1 인덱스에서 도는 것으로 변경

T = int(input())

for t in range(1, T+1):
    n, m = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(n)] # 매트릭스를 생성

    max_sum = 0 # max_sum의 초기값 0으로 설정
    for i in range(n-m+1): # n=5, m=2 이면 i가 0, 1, 2, 3 만약, i가 0일 때
        for j in range(n-m+1): # j는 0
            sum_score = 0
            for row in range(m): # row 0, 1
                for col in range(m): # col 0, 1
                    sum_score += matrix[i+row][j+col] # 즉, matrix[0][0] matrix[0][1] matrix[1][0] matrix[1][1]
                    # 이렇게 돌고나면 j가 1로 변하고 sum_score = 0으로 초기화 
                    # matrix[0][1] matrix[0][2] matrix[1][1] matrix[1][2]
                    # 이렇게 j를 3까지 다 돈 다음 i가 1로 변경 후 또다시 반복
            if sum_score > max_sum: # j가 0에서 1로 변하기 전에 만약 sum_score가 max_sum보다 크다면 max_sum에 새로 sum_score을 할당해준다
                max_sum = sum_score
    
    print(f'#{t} {max_sum}')
            


    

