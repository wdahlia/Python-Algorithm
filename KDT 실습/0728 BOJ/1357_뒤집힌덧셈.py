
# 슬라이싱 이용한 방법
X, Y = input().split()

X = int(X[::-1])
Y = int(Y[::-1])

result = str(X+Y)[::-1]
result = int(result)
print(result)

# len길이에서 인덱스 빼서 하는법
X, Y = input().split()

a = len(X)
b = len(Y)

new_x = ''
for i in range(a):
    new_x += X[(a-1)-i]

new_y = ''
for j in range(b):
    new_y += Y[(b-1)-j]

res = int(new_x) + int(new_y)
res = str(res)
length = len(res)

result = ''
for k in range(length):
    result += res[(length-1)-k]

print(int(result))
# 84ms
