

# 반복되는 문자 input에 내가 넣어 없애는 방법
r = input()
word = 'apple'
n = 0
for str in word:
    if r in word[n]:
        n += 1
    else:
        print(word[n],end='')
        n += 1
# 코드가 지저분한 편

# 코드 수정
r = input()
word = 'apple'
for str in word:
    if r not in str:
        print(str, end='')

# input으로 넣을 수 있게끔 선생님이 가르쳐 준 것 변형
r = input()
word = 'apple'
result = ''
for char in word:
    if r not in char:
        result = result + char 
print(result)

# 선생님이 작성해 보여주신 코드
word = 'apple'
result = ''
for char in word:
    if char != 'a':
        result = result + char
print(result)

# 문자 자체를 input에 넣어 입력하고 반복문에 a가 없는 경우를 출력
r = input()
for char in r:
    if char != 'a':
        print(char, end ='')

