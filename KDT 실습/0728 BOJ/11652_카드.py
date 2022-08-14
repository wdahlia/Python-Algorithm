
import sys
sys.stdin = open('11652.txt')

# 카드 주어질 때, 가장 많이 가지고 있는 정수
# 여러가지라면, 작은 것 출력

N = int(input())

number = dict()                 # 딕셔너리 만들어줌

for _ in range(N):              # 순회하면서 input()값 받아주고
    n = int(input())
    if n not in number:         # 그 값이 number에 없다면 key에 n을 넣어주고 value에 1 초기값 넣어줌
        number[n] = 1
    else:                       # 있다면, value값에 1씩 더해준다
        number[n] += 1

result = sorted(number.items()) # 정렬을 해준다 그럼 리스트안에 튜플형태로 저장
max_num = max(number.values())  # value값들의 max값을 찾아준다

for res in result:              # result함수를 순회하면서
    if res[1] == max_num:       # max값과 튜플의 (정수, 정수의 개수) 중 정수의 개수가 최대값과 같다면
        print(res[0])           # 정수를 출력
        break                   # 가장 작은 값을 출력하라고 했으므로 한 번만 출력하고 break
    