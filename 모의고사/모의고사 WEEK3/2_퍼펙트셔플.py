
import sys
sys.stdin = open("_퍼펙트셔플.txt")

# 우선 반절씩 나눠주어야 함

from collections import deque

T = int(input())

list_1 = deque()
list_2 = deque()

print(list_1)

for n in range(1, T+1):
    num = int(input())
    cards_n = input().split()
    if num % 2 == 0:
        half = num // 2
        list_1 = deque(cards_n[:half])
        list_2 = deque(cards_n[half:])
    else:
        list_1 = deque(cards_n[:half+1])
        list_2 = deque(cards_n[half+1:])

    result_deck = [0] * num
    for i in range(num):
        if i % 2 == 0:
            result_deck[i] = list_1.popleft()
        else:
            result_deck[i] = list_2.popleft()

    print(f'#{n}', *result_deck)
    