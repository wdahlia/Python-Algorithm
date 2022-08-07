import sys
sys.stdin = open('유학금지.txt')

word = input()
for char in 'CAMBRIDGE':
    word = word.replace(char, '')
print(word)