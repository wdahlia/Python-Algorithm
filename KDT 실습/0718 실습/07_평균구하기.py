
# 오류 코드
'''
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

'''

# output : 5.5


# count를 들여쓰기를 안하면 for문이 모두 반복되고 종료된 후 count += 1이 되는 것
# 소수점 자리까지 표현하고 싶다면 / 한번만 쓰면 됨

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

