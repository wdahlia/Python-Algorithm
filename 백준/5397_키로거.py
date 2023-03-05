
tc = int(input())

for _ in range(tc):
  strings = input().rstrip()
  result = []
  s = []

  for char in strings:
    if char == '<':
      if result:
        s.append(result.pop())

    elif char == '>':
      if s:
        result.append(s.pop())

    elif char == '-':
      if result:
        result.pop()

    else:
      result.append(char)
      
  print(*result, sep='', end='')
  print(*s[::-1], sep='')

