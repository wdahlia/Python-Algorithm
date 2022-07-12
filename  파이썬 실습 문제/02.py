
#len() 사용 x

# while문 사용하는 방식

word = input()
n=0
while word[n:]:
    n += 1
print(n)

word = 'hello!'
print(word[1])

# 특정 문자열만 포함되어 있어서 보편적인 방법은 아님!
# input()을 입력하고도 출력되는 코드 구성할 것

word = 'happy!'
n = 0
while(bool(word[n:]) == True):
    n += 1
print(n)

word = "happy!"

cnt = 0
while(word!=""):
    cnt+=1
    word = word[1:]
print(cnt)

# for문 사용

n = 0
word = "happy!"
for i in word:
    n += 1
print(n)



