

# answer이 tuple임 ()
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)


# answer를 리스트로 추가하고 싶은것 이 경우는
# answer에 [] 빈 리스트로 만들어줘야함
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)