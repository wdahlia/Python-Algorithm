
import sys
sys.stdin = open('10773.txt')

# 잘못된 수를 부를 때마다 0을 외침
# 가장 최근에 쓴 수를 지우게 시킨다 - 여기서 stack 이용해야 함을 알 수 있음
# 최종적으로 적어낸 수의 합을 출력

K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    if N > 0:           # N이 0보다 크면
        stack.append(N) # stack에 넣어주고
    else:               # N이 0이면
        stack.pop()     # 맨 끝(즉, 최신 값) pop
        
result = sum(stack)     # 최종 stack의 sum 구함
print(result)
