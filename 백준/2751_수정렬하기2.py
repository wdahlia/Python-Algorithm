
import sys
sys.stdin = open('2751.txt')

# sort가 nlogn의 시간 복잡도 이므로 sort 사용

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()

print(*array, sep='\n')

# 병합 정렬

# 힙 정렬