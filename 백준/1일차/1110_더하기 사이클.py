
N = input()

num = N

num_list = []

while 1:
    if len(num) == 1:
        num = '0' + str(num)
    
    next_num = str(sum(map(int, str(num))))

    num = num[-1] + next_num[-1]
    num_list.append(num)

    if int(num) == int(N):
        break

print(len(num_list))


# 68ms

