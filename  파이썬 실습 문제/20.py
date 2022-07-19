

# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력
# 어제 한 로직과 비슷
# 10으로 나눈 나머지를 사용해서 더해주고 (결과값)
# 그 이후 number을 10으로 나눠준다

number = int(input())
r = 0

while number != 0:
    r += number % 10
    number //= 10
print(r)