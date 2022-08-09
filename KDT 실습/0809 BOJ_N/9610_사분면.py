
import sys
sys.stdin = open('9610.txt')

# 사분면과 축에 점이 몇개 있는가

where = {
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0
}

dots = int(input())

for _ in range(dots):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        where['Q1'] += 1
    elif x > 0 and y < 0:
        where['Q4'] += 1
    elif x < 0 and y < 0:
        where['Q3'] += 1
    elif x < 0 and y > 0:
        where['Q2'] += 1
    else:
        where['AXIS'] += 1

for key, value in where.items():
    print(f'{key}: {value}')
