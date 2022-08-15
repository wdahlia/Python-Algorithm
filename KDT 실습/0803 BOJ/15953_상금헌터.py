
import sys
sys.stdin = open('15953.txt')

# 총 상금을 출력
# 1회 a등, 진출 못했으면 a = 0
# 2회 b등, 진출 못했으면 b = 0

def reward1(x):
    if x == 0 or x >= 22:
        return 0
    elif x < 2:
        return 500
    elif x < 4:
        return 300
    elif x < 7:
        return 200
    elif x < 11:
        return 50
    elif x < 16:
        return 30
    elif x < 22:
        return 10
    
def reward2(y):
    if y == 0 or y >= 32:
        return 0
    if y < 2:
        return 512
    elif y < 4:
        return 256
    elif y < 8:
        return 128
    elif y < 16:
        return 64
    elif y < 32:
        return 32

T = int(input())
for _ in range(T):
    rank1, rank2 = map(int, input().split())
    result = (reward1(rank1) + reward2(rank2)) * 10000
    print(result)

# 리스트에 상금 저장 후 인덱스를 이용하여 푸는 방법 존재할 듯
