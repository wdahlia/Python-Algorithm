
from pprint import pprint 

import sys
sys.stdin = open('2606.txt')

# 한 컴퓨터가 웜 바이러스에 걸리면 네트워크 상에 연결되어 있는 모든 컴퓨터
# 웜 바이러스에 걸림

# 컴퓨터의 수 computers = 7
# 직접 연결 되어 있는 컴퓨터 쌍의 수 즉, 간선
# 연결 되어 있는 컴퓨터의 쌍
# 1번을 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하자


N = int(input())
M = int(input())


matrix = [[] for _ in range(N + 1)]

result = [1]

for _ in range(M):
    start, end = map(int, input().split())
    matrix[start].append(end)
    matrix[end].append(start)


# 동원님 코드 참고

stop = True

while stop:
    length = len(result) # 초기, 탈출 전까지 for문이 끝나고 len을 저장
    for i in result: # result에 해당하는 i 값
        for j in matrix[i]: # matrix에서 i에 해당하는 즉, 그 행을 돌아줌
            if j not in result: # 안에 없다면
                result.append(j)
    if len(result) == length: # 즉, 값이 추가가 안된다는 소리
        stop = False
print(len(result) - 1) # 시작 인덱스를 하나 제외해주어야 함
                