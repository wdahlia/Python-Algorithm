
# a, b를 입력받아
# a를 b로 나눈 몫과 나머지를 출력하는 프로그램 작성

# input : 9 2 ; output : 4 1

# import sys
# sys.stdin = open('2029.txt', 'r')


T = int(input()) 
for i in range(1, T+1): # 이건 나중에 #1 이렇게 표현하기 위함
    q, r = map(int, input().split()) 
    print(f'#{i} {q // r} {q % r}') # 번호, 몫, 나머지 출력
