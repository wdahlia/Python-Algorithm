
# 평균
# 중앙값 

import sys
sys.stdin = open('2587.txt')


list_ = []
for _ in range(6):
    number = int(input())
    list_.append(number)

average = sum(list_) // 5
median = sorted(list_)[2]
# 주어지는 숫자가 5개로 동일하기 때문에

print(average)
print(median)


# 주어지는 숫자가 변동 될 경우 중앙값 찾는 방법
# 올림차순으로 정렬
new_li = sorted(list_)
# 홀수인 경우 가운데 위치한 값이 중앙값 
if len(new_li) % 2 == 1:
    median = new_li[len(new_li) // 2] # 나눈값의 몫의 인덱스가 중앙값

# 5 7 9 10 4
# 올림차순으로 정렬
# 4 5 7 9 10 # 7이 중앙값

# 짝수인 경우 가운데 위치한 두 값의 평균
# 5 7 9 10 4 6
# 4 5 6 7 9 10

else:
    a = new_li[len(new_li) // 2]
    b = new_li[(len(new_li) // 2)-1]
    median = (a + b) / 2 

print(median)
