
import sys
sys.stdin = open('1543.txt')

# 방법 1
line1 = input()
line2 = input()

new = line1.split(line2)

print(len(new)-1) # ['', 'b', 'ba'] split하면 이런 모양이기 때문에 빈칸을 -1 해줌

# 방법2
line1 = input()
line2 = input()
length = len(line2)

idx = 0
cnt = 0

while idx <= len(line1)-length:
    if line1[idx:idx+length] == line2:
        cnt += 1
        idx = idx+length
    else:
        idx += 1

print(cnt)
