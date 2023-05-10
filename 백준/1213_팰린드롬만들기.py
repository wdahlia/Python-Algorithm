
import sys
sys.stdin = open('1213.txt')

# 불가능일때는 I'm Sorry Hansoo 여러개일때는 사전순으로 앞서는거 먼저
# 알파벳 순서를 적절히 바꿔서 만듦

nickname = input()
dict = {}

for alph in nickname:
    if alph not in dict:
        dict[alph] = 1
    else:
        dict[alph] += 1

# 만약에 길이가 홀수번인 애가 1개를 초과해서 만나면 팰린드롬 아님

key_list = sorted(dict.items())

mid = ''
for k, v in key_list:
    if dict[k] % 2:
        if len(mid):
            print("I'm Sorry Hansoo")
            break
        mid = k

else:
    ans = ''
    for k, v in key_list:
        ans += (k * (v//2))

    ans += mid + ans[::-1]

    print(ans)

# for key, value in key_list:
#     if not (dict[key] % 2):
#         ans = ''
#         ans += (key * (value//2))
#         for k, v in key_list:
#             if key != k:
#                 ans += (k * (v//2))

#         ans += mid + ans[::-1]

#         print(ans)

# AAAABBBBC
# AABBCBBAA
# BBAACAABB