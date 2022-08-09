
# a가 처음으로 등장하는 위치 index를 출력하자
# a가 없는 경우에는 -1 출력

# 선생님이 짜주신 코드
# 문자로 순회하는 것이 아닌
# 인덱스로 접근해서 쓰자
# 얻는 방법은? range(len(word)) => 0~5
word = input()
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
    else:
        print(-1)

#내가 짠 코드
word = input()
index = 0
for s in word:
    if s == 'a':
        break
    index = index + 1
else:
    index = -1
    
print(index)

## 중복될때마다 인덱스 표시

# 한번에 표시
word = input()
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end = " ")
        
# 리스트로 표시

# 1. 리스트에 담는다!
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        # 리스트에 추가해줘
        result.append(idx)
print(result)
