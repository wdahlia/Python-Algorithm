# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 우선 전부 다 대문자로 바꾼다음에 대문자 겹치는 문자를 튀어 나오게 하자!


word = input().upper() # 대문자로 바꿔 준다

str_dict = {}
for str in word:
    if str not in str_dict:
        str_dict[str] = 1
    else:
        str_dict[str] += 1

k_list = []
max_v = max(str_dict.values())
for key, value in str_dict.items():
    if value == max_v:
        k_list.append(key)
    
if len(k_list) == 1:
    print(k_list[0])
elif len(k_list) > 1:
    print('?')
# 정답 256 ms 



# 구글링 검색     
word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))])
# 정답 108 ms
