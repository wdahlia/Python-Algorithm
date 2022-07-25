# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 여기서 함정은 Test input 값에 0 0도 포함 0 0은 0으로 출력 안됨
# 0 0인 순간 종료된다. - break
# 인자 간 순회도 아니므로 while문을 사용, 종료문 조건은 a == 0 and b == 0

while True:
    a , b = map(int, input().split())
    if (a == 0 & b == 0):
        break
    else:
        print(a + b)
