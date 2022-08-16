
import sys
sys.stdin = open("_문자열의거울상.txt")

# bdppq > pqqbd
# 즉 끝자리부터 변하기 시작한다는 것
# q -> p p -> q d -> b b -> d

T = int(input()) 

for i in range(1, T+1):

    case = input()                  # 각 문자열을 입력받는다

    case = case[::-1]               # 문자열을 슬라이싱으로 역순으로 출력해준다

    mirror_word = []                # for문을 돌려서 문자가 q p b d 와 같을 떄마다 p q d b로 변환해서 list에 append
    for char in case:
        if char == 'q':
            mirror_word.append('p')
        elif char == 'p':
            mirror_word.append('q')
        elif char == 'b':
            mirror_word.append('d')
        elif char == 'd':
            mirror_word.append('b')
    
    result = ''.join(mirror_word)   # join 메서드 사용해서 결과값을 출력
    print(f'#{i} {result}')
    
# 딕셔너리를 활용한 코드
T = int(input()) 

for i in range(1, T+1):

    case = input()                                      # 각 문자열을 입력받는다

    case = case[::-1]                                   # 문자열을 슬라이싱으로 역순으로 출력해준다

    my_dict = {'q': 'p', 'p': 'q', 'b': 'd', 'd': 'b'}

    mirror_word = [] 
    for char in case:                                   # case를 순환하면서
        mirror_word.append(my_dict[char])
                                                        # my_dict의 char와 일치하는 key의 value값을 mirror_word에 append

    result = ''.join(mirror_word)                       # join 메서드 사용해서 결과값을 출력
    print(f'#{i} {result}')
