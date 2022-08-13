
import sys
sys.stdin = open('7785.txt')

# 어떤 사람이 회사에 들어왔는지 'enter'
# 나갔는지 기록 'leave'
# 현재 회사에 있는 모든 사람(사전 순의 역순으로 기록)
# 동명이인 X, 대소문자 다른 경우 다른 이름

N = int(input())

inout_dict = dict()

for _ in range(N):
    name, inout = input().split()
    if inout == 'enter':
        inout_dict[name] = 0
    else:
        inout_dict[name] += 1

result = sorted(inout_dict.items(), reverse=True)

for r in result:
    if r[1] == 0:
        print(r[0], end = '\n')
        