
import sys
sys.stdin = open('4949.txt')

# ( 는 ) 랑만 짝
# [ 는 ] 랑만 짝
# 균형 잡힌 문자열이 아니라면 no
# 균형 잡힌 문자열이라면 yes
# 마침표 .로 끝남
# 입력의 종료 조건으로 맨 마지막에 점 하나

while True:
    sentence = input()                                  # input을 받아준다
    stack = []                                          # 빈 스택을 만들어줍니다
    
    if sentence == '.':                                 # sentence가 '.' 이라면 break를 걸어준다
        break

    for s in sentence:                                  # sentence를 순환하면서
        if s == '(' or s == '[':                        # 여는 괄호라면 stack에 append 해준다
            stack.append(s)

        if s == ')':                                    # 닫는 괄호일 때
            if len(stack) != 0 and stack[-1] == '(':    # stack이 비어있지 않고, stack의 맨 마지막이 종류가 같은 여는 괄호라면
                stack.pop()                             # pop
            else:   
                stack.append(s)
                break

        elif s == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break

    if len(stack) == 0:                                 # 최종 stack의 길이가 0이라면 yes, 아니라면 no
        print('yes')
    else:
        print('no')
