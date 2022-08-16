
import sys
sys.stdin = open('9093.txt')

# 슬라이싱 이용한 방법 # 772ms
T = int(input())

for _ in range(T):
    sentence = list(input().split())
    words = ''                          # 빈 문자열을 갱신 sentence 받을 때마다
    for word in sentence:               # sentence안의 word들을 순회하면서
        words += word[::-1]             # 빈 문자열에 역으로 슬라이싱한 word들을 넣어주고
        words += ' '                    # 한 칸을 띄어준다

    print(words)                        # 그 과정을 완료한 words를 출력

# 문자열 길이를 이용하여 할 수 있음 # 1180ms
T = int(input())

for _ in range(T):
    sentence = list(input().split())
    words = ''
    for word in sentence:
        for idx in range(len(word)):
            words += word[(len(word)-1)-idx]
        words += ' '
    print(words)

# 슬라이싱과 문자열 길이 이용 # 796 ms
T = int(input())

for _ in range(T):
    sentence = input()
    sentence = sentence[::-1]
    result = sentence.split()
    
    new_sentence = ''
    for idx in range(len(result)):
        res = result[(len(result)-1) - idx]
        new_sentence += res
        new_sentence += ' '
    print(new_sentence)
