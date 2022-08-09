
from pprint import pprint
import sys
sys.stdin = open('2897.txt')

# R행 >= 2, C열 <= 50
# '#' 빌딩 'X' 주차 된 차 '.' 빈 주차 공간
# 차는 2행 2열의 칸을 차지함
# 빌딩이 있는 곳에는 주차X, 주차 공간 없으면 차 부셔도 됨
# 이때, 부수어야하는 차의 수대로 모아 보여줄 것

R, C = map(int, input().split())

matrix = [list(input()) for _ in range(R)] 


dict_ = { # 딕셔너리 구성해 줌
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
}

# 2행 2열의 크기 만큼 차가 주차되니까
# 델타 탐색을 구성 (지금 인덱스 포함)
# 시계 방향
dx = [0, 0, 1, 1] 
dy = [0, 1, 1, 0]

n = len(dx)

for x in range(R-1): # 범위를 벗어나지 않게 탐색하기 위해 -1
    for y in range(C-1):
        cnt_X = 0 
        # cnt_s = 0
        for i in range(n):
            nx = x + dx[i]
            ny = y + dy[i]

            if matrix[nx][ny] == '#': #이 등장하면
                # cnt_s += 1 
                # 원래는 break 걸려고 했는데
                # 답이 안나와서 모든 상황 가정, 해결 완료
                break
            elif matrix[nx][ny] == 'X': # X가 등장하면
                cnt_X += 1

        else:
            dict_[cnt_X] += 1
        # 이런식으로 상황을 가정하면 되었음
        # 상희님 코드를 참고

        # else의 상황에 아래 코드가 모두 포함
        # if cnt_s >= 1:
        #     continue
        # elif cnt_X == 0:
        #     dict_[cnt_X] += 1
        # elif cnt_X > 0:
        #     dict_[cnt_X] += 1
            

for i in range(5):
    print(dict_[i])
