
import sys
sys.stdin = open('2750.txt')

# sort도 있으나, 버블정렬의 방식으로도 가능
# 버블 정렬은 인접한 인자와 비교하여 정렬을 해주는 것으로

# 버블 정렬
array = []

N = int(input())

for _ in range(N):
    array.append(int(input()))

for i in range(N-1):
    for j in range(N-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(*array, sep='\n')