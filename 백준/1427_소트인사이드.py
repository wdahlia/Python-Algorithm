
import sys
sys.stdin = open('1427.txt')

# 수가 주어질 때, 그 수의 각 자리수를 내림차순으로 정렬

number = list(input())

for i in range(len(number)):
    for j in range(i+1, len(number)):
        maxNumber = max(map(int, number[i:len(number)+1]))
        if int(number[j]) == maxNumber:
            if int(number[i]) < maxNumber:
                number[i], number[j] = number[j], number[i]

result = ''.join(number)

print(result)