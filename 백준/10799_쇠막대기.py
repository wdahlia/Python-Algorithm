
import sys
sys.stdin = open('10799.txt')

from collections import deque

# 자신보다 긴 쇠막대기 위에만 놓일 수 있다
# 완전히 포함되도록 놓지만, 끝점들은 겹치면 안됨
# 레이저는 양 끝점 어느 것과도 겹치지 아니함
# 여는괄호 닫는괄호의 쌍 () 레이저다
# 쇠막대기의 왼쪽 끝은 여는 괄호 (, 오른쪽 끝은 닫힌 괄호 )
# 레이저가 2개이다, 쇠막대는 2+1만큼 잘리게 됨

laser = input().replace('()','#')
stack = []
cnt = ironstickCnt = 0
for i in range(len(laser)):
    if laser[i] == '(':
        cnt += 1
        stack.append(laser[i])
    elif laser[i] == ')':
        if stack[-1] == '(':
            stack.pop()
            ironstickCnt += 1
            cnt -= 1

    else:
        if len(stack) != 0:
            ironstickCnt += cnt

print(ironstickCnt)
