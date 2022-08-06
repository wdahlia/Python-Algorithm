import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 이 문제는 숫자 길이가 정확하게 흰 빈칸의 수와 일치해야지만 단어가 들어감
# 즉 k = 3인데 흰 빈칸의 수가 4이면 그 칸은 sum_cnt에 더해주면 안됨


# 문자의 길이(k) = 3
# 흰칸 1 검은칸 0

T = int(input())

for t in range(1, T+1):
    n, k = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 행 체크
    sum_cnt = 0
    for row in range(n): 
        cnt = 0 # 행이 바뀔 때 마다 cnt 초기화 해주어야 함
        for col in range(n):
            if matrix[row][col] == 0: # 검은색 칸을 만났다
                if cnt == k: # 그때, 카운트가 만약 3이다?
                    sum_cnt += 1 # sum_cnt에 더하고
                cnt = 0 # cnt 초기화 해줌
            else: # 흰칸 만났다
                cnt += 1 # cnt 하나씩 해줌

        if cnt == k: # 만약 행을 다 돌았는데 또 cnt가 3이다
            sum_cnt += 1 # sum_cnt에 1 더해준다 
        # 이 경우를 고려하는 이유는 
        # 검은 칸이와서 초기화 되었는데 뒤에 칸의 cnt가 3(k)일 수 있기 때문

    # 열 체크 - 동일한 방법으로
    # 이 때 주의 할점 sum_cnt = 0 안해줘도 됨
    # 결국 단어를 넣을 수 있는 칸의 총 개수를 구하는 것이므로
    for col in range(n):
        cnt = 0
        for row in range(n):
            if matrix[row][col] == 0:
                if cnt == k:
                    sum_cnt += 1
                cnt = 0
            else:
                cnt += 1
                
        if cnt == k:
            sum_cnt += 1


    print(f'#{t} {sum_cnt}')