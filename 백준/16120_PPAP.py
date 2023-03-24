
# P는 PPAP 문자열
# p에서 시작해서 p를 PPAP로 바꾸는 과정
# PPAP 문자열이면 PPAP, 아니면 NP

word = input()

stack = []

for i in range(len(word)):
  if stack:
    if len(stack) >= 4:
      w = ''.join(stack[-4:])
      if w == 'PPAP':
        for _ in range(4):
          stack.pop()  
        stack.append('P')
    stack.append(word[i])
  else:
    stack.append(word[i])

if (stack == ['P']) or (''.join(stack) == 'PPAP'):
  print('PPAP')
else:
  print('NP')
