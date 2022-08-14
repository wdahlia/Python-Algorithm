
import sys
sys.stdin = open('10816.txt')

# 상근이가 가지고 있는 숫자 카드의 개수 N
# 숫자 카드에 적혀 있는 정수
# 몇 개 가지고 있는 숫자 카드인지 구해야할 M개의 정수
# 공백 구분 출력

N = int(input())
cards_n = list(map(int, input().split()))
M = int(input())
cards_m = list(map(int, input().split()))

for card2 in cards_m:       
    cnt = 0                 # 다음 인덱스로 넘어가기전에 cnt 초기화
    for card1 in cards_n:  
        if card2 == card1:  # 같다면
            cnt += 1        # 1씩 더해준다
    print(cnt, end= ' ')
# 시간초과 - 이중 for문은 안될듯

# 딕셔너리로 풀이
result = dict()

for card2 in cards_m:
    if card2 not in result:
        result[card2] = 0

for card1 in cards_n:
    if card1 in result:
        result[card1] += 1

for i in range(M):
    print(result.get(cards_m[i]), end = ' ')    # key 값에 해당하는 value 값들을 출력
