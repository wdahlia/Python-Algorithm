
import sys
sys.stdin = open('1371.txt')
# 알파벳 순으로 출력이 문제
# 딕셔너리로 하는 방법이 있긴 하겠지만
# 너무 많이 작성
# ascii code 사용

import sys

# ascii 코드

alph = [0] * 26

sentence = sys.stdin.read().split()
 
for s in sentence:
    for char in s:
        alph[ord(char)-97] += 1

l = len(alph)
max_ = max(alph)

for idx in range(l):
    if alph[idx] == max_:
        result = chr(97 + idx)
        print(result, end='') 

# 딕셔너리 코드

alph = 'abcdefghijklmnopqrstuvwxyz'

alph_dict = dict()

for char in alph:
    if char not in alph_dict:
        alph_dict[char] = 0

sentence = sys.stdin.read().split()

for word in sentence:
    for w in word:
        alph_dict[w] += 1

max_cnt = max(alph_dict.values())

for k, v in alph_dict.items():
    if v == max_cnt:
        print(k, end = '')
