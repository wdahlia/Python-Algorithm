
import sys
sys.stdin = open('3273.txt')

# 쌍의 개수를 출력하는 문제
# 투 포인터 

def twopointer(left, right):
    resultCnt = 0
    while left < right:
        if array[left] + array[right] == target:
            resultCnt += 1
            left += 1

        elif array[left] + array[right] > target:
            right -= 1

        else:
            left += 1

    print(resultCnt)

N = int(input())
array = list(map(int, input().split()))
target = int(input())
array.sort()

left = 0
right = N-1

twopointer(left, right)
