

# 주어진 수 n이 3의 배수이면서 짝수인 경우
# 참, 거짓 출력

num = int(input())
if num % 3 == 0 and num % 2 == 0:
    print('참')
else:
    print('거짓')