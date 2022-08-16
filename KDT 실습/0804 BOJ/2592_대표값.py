
import sys
sys.stdin = open('2592.txt')

# 평균과 최빈값 출력
# 최빈값이 둘 이상인 경우 그 중 하나만 출력
# 줄은 10개 주어짐

# 딕셔너리 풀이
T = 10

num_dict = dict()
for _ in range(T):
    number = int(input())
    if number not in num_dict:
        num_dict[number] = 1
    else:
        num_dict[number] += 1

sum_num = 0
for key, value in num_dict.items():
    sum_num += (key * value)
avg = sum_num // T
print(avg)
    
max_num = max(num_dict.values())
for key, value in num_dict.items():     # 최빈값이 2개 이상인 경우 그 중 하나만 출력
    if value == max_num:
        print(key)
        break            # 딱히 우선순위가 있는건 아니여서 한 개 출력 후 break 걸어줌
