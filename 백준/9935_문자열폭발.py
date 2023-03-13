
# 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다
# 폭발 문자열 포함하는 경우 모든 폭발 문자열이 폭발, 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다
# 문자열에 없을 때까지 계속(while문 써라는 힌트일 수도)
# 남아있는 문자 없다면 'FRULA' 출력
# 같은 문자 두개 이상 포함하지 않음

word = input()
string = input()
l = len(string)
stack = []
result = ''

for i in range(len(word)):
  stack.append(word[i])
  if stack[-1] == string[l-1] and ''.join(stack[-l:]) == string:
    for _ in range(l):
      stack.pop()

if not len(stack):
  result = 'FRULA'
else:
  result = ''.join(stack)

print(result)
