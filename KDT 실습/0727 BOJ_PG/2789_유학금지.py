
import sys
sys.stdin = open('2789.txt')

word = input()
for char in 'CAMBRIDGE':
    word = word.replace(char, '')
print(word)
