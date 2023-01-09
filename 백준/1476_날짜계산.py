
import sys
sys.stdin = open('1476.txt')

# E는 15까지 S는 28까지 M은 19까지

e, s, m = map(int, input().split())

num = max(e, s, m)

while 1:
    if ((num - e) % 15 == 0) and ((num - s) % 28 == 0) and ((num - m) % 19 == 0):
        print(num)
        break
    num += 1

