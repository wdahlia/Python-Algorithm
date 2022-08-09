import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

# 5 - 수강생 수 3 - 과제 제출한 수

for t in range(1, T+1):
    result = []
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    # 방법 1
    for i in range(1, n+1): # 원래 이렇게 풀면되는 간단한 문제
        if i not in arr:
            result.append(i)

    # 방법 2 굳이 [0] * n 만들어서 풀어봄
    matrix = [0] * n # 0이 수강생 수만큼 있는 이루어진 리스트를 만들어 준다 [0, 0, 0, 0, 0]

    for i in range(n):
        for a in arr: 
            if i == a-1: # 정수 1-N까지 였으므로 만약 1이다 그럼 인덱스 0에 들어가야지 오름차순으로 정렬됨 즉 i == a-1이랑 같으면
                matrix[i] = a # a 값을 matrix의 i 인덱스에 할당
        # if matrix[i] == 0: # for문을 돈 후의 matrix[i]가 0인 값이 있다면
        #     result.append(i+1) # 394ms result 인덱스에 append 해줍니다

    for j in range(n): 
            if matrix[j] == 0:
                result.append(j+1) # 이게 실행이 더빠르다 371ms

  
    print(f'#{t}', *result)






            


    