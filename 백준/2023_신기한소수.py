
import sys
sys.stdin = open('2023.txt')

# 소수 7331
# 왼쪽에서부터 1자리, 2자리, 3자리, 4자리가 다 소수
# 이것을 신기한 소수
# 자릿수의 개념으로 dfs 접근
# 1의 자리숫자 즉, 10보다 작은 소수는 2 3 5 7
# 2째 자리 수부터는 홀수이어야함 1 3 5 7 9

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

number = int(input())

def dfs(x):

    decimal = str(x)

    if len(decimal) == number:
        print(decimal)
    elif len(decimal) > number:
        return
    else:
        for i in range(1, 10, 2):
            num = (10 * int(decimal)) + i
            switch = True
            for n in range(3, num, 2):
                if num % n == 0:
                    switch = False
                    break
            if switch:
                dfs(num)
                          
dfs(2)
dfs(3)
dfs(5)
dfs(7)
