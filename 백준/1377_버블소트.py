
import sys
sys.stdin = open('1377.txt')

# N은 배열의 크기 A는 정렬해야 하는 배열
# 10 1 5 2 3
#  0 1 2 3 4 - 정렬 전 인덱스
# 1 5 2 3 10  A[1]
# 1 2 3 5 10  A[2]
# 1 2 3 5 10  A[3] 즉 A가 3일 때 정렬이 완료된 것을 확인 가능 루프를 1번 더 돌려주어야함
# 1 3 4 2 0 - 정렬 후 인덱스
# N = 500,000 이므로 버블소트를 하게된다면 2초를 넘게 됨

N = int(input())
array = [(int(input()), idx) for idx in range(N)]
sortArray = sorted(array)

maxChange = 0
for i in range(N):
    indexChange = sortArray[i][1] - array[i][1]
    if indexChange > maxChange:
        maxChange = indexChange

print(maxChange + 1)
