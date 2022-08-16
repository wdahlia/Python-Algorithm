import sys

sys.stdin = open("_반반.txt")

# 각 행마다 두개의 서로 다른 문자 등장
# 각 문자가 정확히 두 번 등장하는 지 판별


T = int(input())

for n in range(1, T+1):
    cnt = 0
    word = input()
    alph_dict = dict()
    
    for i in word:
        if i not in alph_dict:
            alph_dict[i] = 1
        else:
            alph_dict[i] += 1
            if alph_dict[i] == 2:
                cnt += 1
        print(cnt)

    if len(alph_dict.values()) == 2 and cnt == 2:
        print(f'#{n} Yes')
    else:
        print(f'#{n} No')
            
    