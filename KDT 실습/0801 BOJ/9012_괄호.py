import sys
sys.stdin = open('9012_괄호.txt')

T = int(input())


for _ in range(T):
    bracket = input()
    stack = []
    for b in bracket:
        if b == '(':
            stack.append(b)
        else:
            if '(' in stack:
                stack.pop()
            else:
                stack.append(b)

    if len(stack) != 0 :
        print('NO')
    else:
        print('YES')

    