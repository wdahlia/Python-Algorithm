
import sys
sys.stdin = open('1288.txt', 'r')


# 0 - 9까지 전부 세었을떄 카운트를 종료.


T = int(input())
for l in range(1, T+1):
    num = int(input())
    num1 = num
    sleep_list = [] * 10
    while len(sleep_list) < 10:
        for n in str(num):
            if n not in sleep_list:
                sleep_list.append(n)
        if len(sleep_list) == 10:
            break
        num += num1
    print(f'#{l} {num}')
