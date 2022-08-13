
# a, b, c 입력하여 int로 변환 후 곱셈한 결과를 str으로 변환하여 multiply_abc 변수에 저장
a = int(input())
b = int(input())
c = int(input())

multiply_abc = str(a * b * c)

# global ; i가 예를 들어 range(10) 0-9 중 0 일때,
# local ; for 문인 multiply_abc안의 문자열을 순회하며 char를 int 타입으로 바꿔 i와 비교
# 즉, 0이 있다면 cnt에 1을 추가
# 그래서 local을 모두 순회하면 print(cnt)
# 모든 순회가 끝나고 global ; 1로 넘어갈때 cnt는 다시 0으로 초기화 되고 순회
# range(10)가 끝날때 까지 순회하면서 cnt를 계속 출력
for i in range(10):
    cnt = 0
    for char in multiply_abc:
        if int(char) == i:
            cnt += 1
    print(cnt)
    