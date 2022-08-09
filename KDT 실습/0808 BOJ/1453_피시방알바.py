
# input
'''
5
1 2 3 2 2
'''
# output : 0

import sys
sys.stdin = open('1453.txt')

N = int(input())

want = list(map(int, input().split()))

# 방법 1
seat = []
cnt = 0
for idx in range(N):
    if want[idx] not in seat: # seat안에 값이 없다면
        seat.append(want[idx]) # 추가
    else: # 있다
        cnt += 1 # 못 앉는 사람 수 1명 증가
print(cnt)

# 방법 2 원 리스트에서 - 중복숫자 제거한 리스트의 길이 = 앉지 못하는 사람의 수 나옴
result = len(want) - len(set(want))
print(result)
