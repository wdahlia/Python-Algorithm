
import sys
sys.stdin = open('11652.txt')

# 카드 주어질 때, 가장 많이 가지고 있는 정수
# 여러가지라면, 작은 것 출력

N = int(input())

number = dict()

for _ in range(N):
    n = int(input())
    if n not in number:
        number[n] = 1
    else:
        number[n] += 1

result = sorted(number.items())
max_num = max(number.values())

for res in result:
    if res[1] == max_num:
        print(res[0])
        break
    