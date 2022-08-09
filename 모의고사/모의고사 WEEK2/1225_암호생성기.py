import sys

sys.stdin = open("_암호생성기.txt")

# 문제를 읽자마자 deque를 사용하면 된다고 생각
# 맨 첫번째 인덱스를 빼서 맨뒤쪽으로 보낼때 -1, -2, -3, -4, -5 한 값을 보내고
# 이게 한번의 주기임
# while문 안에 for문을 사용해서 주기 표현
# while문은 password[-1]이 0이 아닐때, 즉 password[-1] = 0이 되면 while문 종료

from collections import deque

T = 10
for t in range(1, T+1):
    T = int(input())
    password = deque(list(map(int, input().split())))

    while password[-1] != 0: # 사이클을 계속 반복해야 함 0보다 작거나 같을 때 까지
        for i in range(1, 6):
            if password[-1] <= 0:
                password[-1] = 0
                # break
            else: # password[-1] > 0인 경우
                new = password.popleft() 
                password.append(new - i)
        
    print(f'#{t}', *password)