
import sys
sys.stdin = open('1855.txt')

# 암호화 되 있는 문자, 몇개의 열로 암호를 하였는지 주어지면 원래의 문자열을 구하라

col = int(input())
text = input()

result = []
for idx in range(0, len(text), col):
    result.append(text[idx:idx+col])

for i in range(len(result)):
    if i % 2 == 1:
        result[i] = result[i][::-1]

res = ''
for j in range(col):
    for k in range(len(result)):
        res += result[k][j]

print(res)