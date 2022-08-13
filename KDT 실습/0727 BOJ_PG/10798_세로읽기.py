
import sys
sys.stdin = open('10798.txt')

# 세로로 출력할 때 빈칸이 있으면 빈칸은 건너뛰고 출력할 것
arr = []
for _ in range(5):
    T = list(input())
    arr.append(T)               # 우선 인풋 받은 값들을 모두 저장해주어야함

for col in range(15):           # 각 줄에 최소 1개, 최대 15개의 글자들이 빈칸없이 연속으로 주어짐 # 즉 열 최대 15
    for row in range(5):
        if col < len(arr[row]): # 열 인덱스가 행의 총 길이보다 작을 때까지 프린트
            print(arr[row][col], end='') 
