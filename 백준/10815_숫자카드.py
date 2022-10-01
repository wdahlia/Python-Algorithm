
import sys
sys.stdin = open('10815.txt')

# 2초라는 시간 제한, n, m개의 정수 최대 500,000가 주어지는데 이걸 순회를 한다고 치면 n 제곱, 즉 시간초과
# 파이썬은 초당 2000만번의 연산 가능
# 이분탐색으로 풀이

def binarySearch(start, end, target):
    mid = (start + end) // 2
    if start > end:
        return 0
    else:
        if arrayList[mid] == target:
            return 1
        elif arrayList[mid] > target:
            # 이 경우는 즉 target 보다 arrayList[mid] 값이 크다는 것 즉 mid가 오른쪽에 있다 이경우는 오른쪽은 탐색 필요 x
            return binarySearch(start, mid - 1, target)
        elif arrayList[mid] < target:
            # 이 경우는 즉 target이 arrayList[mid]보다 오른쪽에 위치 이 경우는 왼쪽 탐색이 필요없음 mid + 1 더해주고 그걸 start로 하자
            return binarySearch(mid + 1, end, target)


N = int(input())
arrayList = list(map(int, input().split()))

M = int(input())
targetList = list(map(int, input().split())) 

arrayList.sort()

for num in targetList:
    start = 0
    end = len(arrayList) - 1
    target = num
    print(binarySearch(start, end, target), end=' ')
