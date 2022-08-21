
import sys
sys.stdin = open('6996.txt')

T = int(input())

for _ in range(T):
    word1, word2 = input().split()

    w1 = sorted(list(word1)) # sorted() 사용하면 알파벳 정렬가능 # 문자열 list로 형 변환하면 각각 문자열 분리 가능
    w2 = sorted(list(word2)) 

    if w1 == w2:
        print(f'{word1} & {word2} are anagrams.')
    else:
        print(f'{word1} & {word2} are NOT anagrams.')
        