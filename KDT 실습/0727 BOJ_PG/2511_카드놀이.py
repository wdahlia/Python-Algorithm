
import sys
sys.stdin = open('2511.txt')

# 고려해야하는 사항
# 1. 총합이 큰 사랑이 우승
# 2. 모든 게임을 비길 경우 (이 말의 즉슨 모든 게임마다 A,B가 동일한 점수였다는 것) 에만 D를 출력
# 3. 그 외 총합이 같다면 마지막 게임에서 이긴 사람이 우승

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = sum_B = 0 
if A == B:                      # A = B 리스트가 같은 경우 즉 모든 sum_A와 sum_B의 합이 10임
    print(10, 10)               # 이 경우 10, 10을 프린트하고 # D를 출력
    print('D')
else:
    for idx in range(10):       # 총 10번의 경기를 한다고 했으므로
        if A[idx] > B[idx]:     # 요소마다 비교
            sum_A += 3
            winner = 'A'        # 이긴 사람들을 계속 winner에 저장해주면서 갱신해줌
        elif A[idx] < B[idx]:
            sum_B += 3
            winner = 'B'
        else:                   # 비길 경우
            sum_A += 1 
            sum_B += 1

    print(sum_A, sum_B)         # 먼저 총합을 프린트해주고

    if sum_A == sum_B:          # 만약 총합이 같다면
        print(winner)           # 마지막 winner를 출력
    elif sum_A > sum_B:
        print('A')
    elif sum_A < sum_B:
        print('B')
        