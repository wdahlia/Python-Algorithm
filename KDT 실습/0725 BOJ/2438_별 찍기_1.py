
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 숫자를 입력하면
T = int(input())

# 1부터 입력한 숫자 + 1의 범위 네에서 star에 i를 곱한 값 만큼
# star를 출력해주세요
for i in range(1, T+1):
    star = '*'
    star = star * i
    print(star)
    