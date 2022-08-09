
# 10개의 수를 입력 받아, 평균값을 출ㄹ력
# 소수점 첫째 자리에서 반올림한 정수 출력
# input : 3 17 1 39 8 41 2 32 99 2 ; output : 24

# import sys
# sys.stdin = open('2071.txt', 'r')

T = int(input())

for i in range(1, T+1):
    a = list(map(int, input().split()))
    if a:
        b = sum(a[::])/len(a) # 리스트의 처음부터 끝까지 슬라이싱한 값을 sum 그걸 리스트의 길이로 나눔
        print(f'#{i} {round(b)}') # 출력값이 반올림한 정수니까 round를 써줌


## sum 함수 안쓰고 for문으로 

for i in range(1, T+1):
    l = 0 # 인덱스가 변화할 때마다 두 변수를 초기화
    s = 0
    num = list(map(int, input().split()))
    for n in num: # 리스트 안을 순회하면서
        s += n # 그 값을 s에 더해주고
        l += 1 # 각 요소의 개수를 구하기 위해 1씩 더해줌
    result = s/l
    print(f'#{i} {round(result)}')
