

# 소문자로 구성된 문자열 word가 주어질 때,
# 모두 대문자로 바꾸어 표현
# 추가 정보를 참고하여
# str이 word에 포함될때
# 유니코드 숫자로 변환하여 
# 다시 문자로 재변환하도록

word = input()
for str in word:
    a = ord(str)
    b = chr(a-32)
    print(b, end='')
