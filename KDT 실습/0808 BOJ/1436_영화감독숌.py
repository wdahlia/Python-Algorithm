
import sys
sys.stdin = open('1436.txt')

T = int(input())

result = 666
while T > 0:
    if '666' in str(result):
        if T == 1:
            break
        else:
            T -= 1
            result += 1
    else:
        result += 1

print(result) 
