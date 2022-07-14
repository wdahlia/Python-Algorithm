
# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

i = input()
print(i[::-1])

# 선생님이 풀어주신 방법 
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')