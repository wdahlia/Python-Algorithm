# N개의 정수가 주어짐
# 최솟값과 최댓값을 구하는 프로그램을 작성하시오

N = int(input()) # N개의 정수 주어짐

num_list = list(map(int, input().split()))

# 최대값 구하는 프로그램
max_n = num_list[0]
for num in num_list:
    if num > max_n:
        max_n = num

# 최소값 구하는 프로그램
min_n = num_list[0]
for num_ in num_list:
    if num_ < min_n:
        min_n = num_

print(f'{min_n} {max_n}')

# 이렇게 하니까 실행시간이 생각보다 너무 길다 # 520ms

N = int(input()) # N개의 정수 주어짐

num_list = list(map(int, input().split()))

# 최대, 최소 동시에 if else 문을 생각했었는데 그게 아니고
# if elif로 동시에 돌리면 그만이었다.
max_n = num_list[0]
min_n = num_list[0]
for num in num_list:
    if num > max_n:
        max_n = num
    elif num < min_n:
        min_n = num

print(min_n, max_n)

# 516ms 별 차이가 없다


# 마지막 max, min 내장 함수 사용

N = int(input()) # N개의 정수 주어짐

num_list = list(map(int, input().split()))

print(min(num_list), max(num_list))

# 404ms 제일 짧다.
    