remain_list = {}
for i in range(10):
    num = int(input())
    remain_num = num % 42
    if remain_num not in remain_list:
        remain_list[remain_num] = 1
    else:
        remain_list[remain_num] += 1

result = len(list(remain_list.values()))
print(result)

# 정담 72ms
