
import sys
sys.stdin = open('1234.txt')

#1 1234
#2 4123
#3 123123
#4 1234123123
#5 12341
#6 123535
#7 123432141
#8 231231321
#9 12312323
#10 9823

# 같은 번호로 붙어있는 쌍을 소거 남은 번호를 비밀번호로 만드는 것

T = 10

for idx in range(1, T+1):
    N, numbers = input().split()
    N = int(N)
    stack = []
    
    for i in range(N):
        if not stack:                       # 비어있다면
            stack.append(numbers[i])
        else:                               # 있다면
            if numbers[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(numbers[i])
    
    print(f'#{idx}', end=' ')
    print(*stack, sep='')
    