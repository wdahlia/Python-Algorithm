

n = int(input())

a = 0

# n을 10씩 나눌 때 마다 a에 1을 추가
while n > 0:
    n //= 10
    a += 1

print(a)