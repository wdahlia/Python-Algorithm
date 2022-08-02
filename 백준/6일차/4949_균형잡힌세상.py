import sys
sys.stdin = open('4949_균형잡힌세상.txt')

# while 1:
#     sentence = input().split()
#     if sentence == '.':
#         break

#     stack = []

#     for s in sentence:
#         if s == '(' or s == '[':
#             stack.append(s)
#         else:
#             if s == ')' or s == ']':
#                 stack.pop()
#                 if len(stack) == 0:
#                     break

# if len(stack) == 0:
#     print('yes')
# else:
#     print('no')