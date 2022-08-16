
import sys
sys.stdin = open('1547.txt')

# 컵의 순서는 왼쪽 컵부터 1번, 2번, 3번
# 위치를 M번 바꾼 이후 공이 들어있는 컵의 번호 출력
# 바꾼 방법 X와 Y가 주어짐
# X와 Y가 같을 수도 있음
# 공이 사라진 경우는 -1 출력
# 인덱스 맞추고 싶으면 0,1,2,3 해도 될 듯

li = [1, 2, 3]

M = int(input())

for _ in range(M):
    x, y = map(int, input().split())
    li[x-1], li[y-1] = li[y-1], li[x-1]

L = len(li)
for idx in range(L):
    if li[idx] == 1:
        print(idx+1)
    elif 1 not in li:
        print(-1)
