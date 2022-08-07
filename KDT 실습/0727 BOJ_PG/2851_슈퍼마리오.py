
import sys
sys.stdin = open('슈퍼마리오.txt')

# 값은 나오는데, 백준에서는 틀리다고 나옴 왜 그럴까?
# 아마 변수값 지정을 안해줘서 그런듯 싶다.

score_list = []

for i in range(10):
    score_list.append(int(input()))

sum_list = []
sum_score = 0 
for score in score_list:
    sum_score += score
    sum_list.append(sum_score)

for s in range(1, 10):
    past_idx = sum_list[s-1]
    now_idx = sum_list[s]
    if now_idx >= 100:
        if now_idx - 100 <= 100 - past_idx:
            print(now_idx)
            break
        else:
            print(past_idx)
            break
else:
    print(sum_list[9])
# 정답처리 68ms

score_list = []
for i in range(10):
    score_list.append(int(input()))
    
score = 0
for s in range(10):
    past_score = score
    score += score_list[s]
    if score >= 100:
        over = score - 100
        under = 100 - past_score
        if over <= under:
            print(score)
            break
        else:
            print(past_score)
            break
else:
    print(score)
# 정답처리 된 답 76ms
    
# dict으로 푸는 법 그냥 구상해볼 것
score_list = []

for i in range(10):
    score_list.append(int(input()))

sum_list = []
sum_score = 0 
for score in score_list:
    sum_score += score
    sum_list.append(sum_score)

dif = 0
dif_dict = {}
for s in sum_list:
    if s > 100:
        dif = s - 100
        dif_dict[dif] = s
        min_ = min(dif_dict.keys())
        if dif <= min_:
            print(s)
            break
        elif dif > min_:
            print(dif_dict[min_])
            break
    elif s == 100: 
        print(s)
        break
    else:
        dif = abs(s - 100)
        dif_dict[dif] = s
else:
    print(sum_list[9])
