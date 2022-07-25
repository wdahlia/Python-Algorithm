
# 두 정수 A, B 주어질 때, A와 B를 비교하는 프로그램

a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

