
# 리스트로 푸는 법
alpha_word = input()

dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

for word in alpha_word:
    for i in range(len(dial_list)):
        if word in dial_list[i]:
            cnt += i + 3

print(cnt)
# 68ms


# dictionary로 하는 방법도 존재
alpha_word = input()

dial_dict = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXYZ' : 10
}

sum = 0
for word in alpha_word:
    for dial in dial_dict:
        if word in dial:
            sum += dial_dict[dial]

print(sum)
# 72ms 
