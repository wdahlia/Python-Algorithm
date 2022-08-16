
import sys
sys.stdin = open('2669.txt')
# 네 개의 직사각형이 차지하는 면적을 출력
# 즉, 겹치는 부분이 있다면 제거 해주어야 함
# 한 좌표당 면적은 1이다를 활용하자

matrix = [[0] * 100 for _ in range(100)]

cnt = 0
for _ in range(4):
    r1, c1, r2, c2 = list(map(int, input().split()))
    for i in range(r1, r2):
        for j in range(c1, c2):
            if matrix[i][j] == 0:
                cnt += 1
                matrix[i][j] += 1
            if matrix[i][j] == 1:
                pass

print(cnt)
