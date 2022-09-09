
import sys
sys.stdin = open('2476.txt')

N = int(input())

result = []
for _ in range(N):
    dice = list(map(int, input().split()))
    dice_set = list(set(dice))
    if len(dice_set) == 1:
        num = 10000 + (dice_set[0] * 1000)
        print(dice_set)
    elif len(dice_set) == 2:
        for i in dice_set:
           if dice.count(i) == 2:
            num = 1000 + (i * 100)    
    else:
        mx = max(dice_set)
        num = mx * 100
             
    result.append(num)

print(max(result))