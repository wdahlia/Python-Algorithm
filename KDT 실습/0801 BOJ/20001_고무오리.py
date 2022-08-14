
import sys
sys.stdin = open('20001.txt')

# 최근에 풀던 백준 문제를 해결해주는 능력
# '고무오리' 받으면 최근 풀던 문제 해결
# '고무오리 디버깅 끝' 문제풀이 종료
# '고무오리' 풀 문제 없는데 사용하면 벌칙으로 두 문제 추가
# 모든 문제 해결 - 고무오리야 사랑해
# 문제 남으면 - 힝구

stack = []

while 1:                                # while문 사용
    problem = input()                   # 입력값 받을 때
    if problem == '고무오리 디버깅 시작':    # 고무오리 디버깅 시작 받으면 시작 continue로 통과해줌
        continue
    elif problem == '문제':              # '문제'를 만나면 stack에 추가
        stack.append(problem)
    elif problem == '고무오리':           # '고무오리'를 만나면, stack안에 '문제'가 없을 때, 벌칙으로 두 문제 추가
        if '문제' not in stack:
            stack.append('문제')
            stack.append('문제')
        else:                           # '문제'가 있다면 가장 최근의 문제를 pop해주세요
            stack.pop()
    else:                               # 그 외에 즉, '고무오리 디버깅 끝'을 만난다면 멈춰줌
        break

if len(stack) == 0:                     # stack의 길이가 0이면 즉, 빈 stack이면
    print('고무오리야 사랑해')
else:                                   # 그 외의 경우, stack에 요소가 있다면
    print('힝구')
    