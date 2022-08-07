
# 양의 정수 number가 주어질 때 # 123
# 숫자의 길이를 구하시오 str() 사용 금지

n = int(input())

a = 0

# n을 10씩 나눌 때 마다 a에 1을 추가
while n > 0:
    n //= 10
    a += 1

print(a)
