
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.

w = input()
n = 0 
for str in w:
    if str == 'a':
        n += 1
print(n)
