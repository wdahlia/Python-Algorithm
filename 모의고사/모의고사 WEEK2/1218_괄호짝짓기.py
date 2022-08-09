# stack을 이용한 문제인데 stack으로 결국은 못풀었다고 봐야할 듯
# (유의할 점) : pop을 했을 때 괄호가 4가지 종류이므로 같은 괄호가 아닌 다른 괄호가 pop 될 수 있다
# b_len = 10
# brackets = ['<', '{', '[', '[', '[', '>', '}', ']', ']', ']'] 
# - 이 경우는 구글링해서 찾아본 파이썬 코드들은 0으로 출력 내가 처음 푼 방법도 SWEA 답은 맞는데 이 케이스를 넣어보면 짝도 다 맞지만 0을 출력한다
# brackets = ['[', ']', ']', '{', '<', '[', '}', '[', '>', ']'] - 의문1? 만약? 짝은 맞는데 ], [ 이런식으로 맞은 경우도 허용해야하는가?
# 문제 답은 맞췄는데 이 상황에는 짝이 전부 맞음에도 0으로 출력이 됨 - 그래서 코드 수정

import sys

sys.stdin = open("_괄호짝짓기.txt")

T = 10

for t in range(1, T+1):
    b_len = int(input())
    brackets = list(input())


    left_right = {  # 딕셔너리를 이용해서 열린괄호를 닫힌 괄호로 바꿔 줄 것이기 때문에 '(' : ')' 이런식으로 구성
        '(' : ')',
        '{' : '}', 
        '[' : ']', 
        '<' : '>'
    }

    stack = []
    for idx in range(b_len): # 주어진 원 리스트 brackets의 길이를 순회 즉, brackets의 index
        if brackets[idx] in left_right.keys(): # brackets[idx]가 key들 즉, '(', '{', '[', '<' 중에 있다면
            stack.append(left_right[brackets[idx]]) # stack에는 딕셔너리의 해당하는 key의 value 값을 ')', '}', ']', '>' 추가
        else: # 만약에 key 값이 아니라면 즉, ')', '}', ']', '>' 일 경우
            if brackets[idx] in stack: # 값이 stack 안에 있다면
                v = stack.index(brackets[idx]) # brackets[idx]랑 일치하는 요소가 처음 등장하는 index를 v에 할당
                stack.pop(v) # 그 인덱스에 해당하는 것을 pop 해준다
            else: # 값이 stack 안에 없다면
                pass # 다음 인덱스로 넘어간다

    result = 1
    if len(stack) != 0:
        result = 0

    print(f'#{t} {result}')



T = 10

for t in range(1, T+1):
    b_len = int(input())
    brackets = list(input())

    dict_left = {
        '(' : 0,
        '{' : 0, 
        '[' : 0, 
        '<' : 0}
    dict_right ={
        ')' : 0,
        '}' : 0,
        ']' : 0,
        '>' : 0
    }


    for idx in range(b_len): # idx를 돌면서 각 키에 해당하는 값이 나오면 1씩 계속 더해주는 것 
        if brackets[idx] in dict_left.keys():
            dict_left[brackets[idx]] += 1
        elif brackets[idx] in dict_right.keys():
            dict_right[brackets[idx]] += 1

    left = list(dict_left.values()) # ( { [ < 각각의 값이 brackets 안에 얼만큼 있는지 그 숫자를 리스트로 뽑아내줌
    right = list(dict_right.values()) # ) } ] > 각각의 값이 brackets 안에 얼만큼 있는지 그 숫자를 리스트로 뽑아내줌


    result = 1 # 값이 같으면 1 출력
    for index in range(len(left)): # len(left) 던지 len(right) 던지 값 똑같음 4써도 될듯
        if left[index] == right[index]: # 각 리스트의 같은 인덱스 끼리 비교해서 값이 같다
            pass
        else:
            result = 0 # 값이 안 같으면 0 출력

    print(f'#{t} {result}')


