
import sys
sys.stdin = open('10546.txt')

# 참가자 수 - N
# 참가자의 이름 - N개의 줄
# 완주한 참가자 - N-1개의 줄
# 동명이인 존재
# 완주하지 못한 참가자 이름 출력

import sys
input = sys.stdin.readline          # 시간 초과 해결

N = int(input())

start = dict()                      # 딕셔너리 이용
for _ in range(N):                  # 참가한 사람의 이름 입력 받아준다
    name = input()
    if name not in start:           # 딕셔너리안에 이름이 없으면 [key : name], [value : 1]을 넣어준다
        start[name] = 1
    else:                           # 있다면 해당 키의 value 값에 1씩 더해준다
        start[name] += 1

for _ in range(N-1):                # 완주한 사람의 이름 입력 받아준다
    finish = input()
    if finish in start:             # 완주한 사람의 이름이 딕셔너리에 이미 있다면
        start[finish] -= 1          # -1씩 해준다 (동명이인 존재, 도착한 사람들 표시 위함)

for key, value in start.items():    # key와 value를 모두 돌면서
    if value == 1:                  # value가 1인 값이 있으면
        print(key)                  # print 해준다
        