
# dictionary를 이용한 풀이
remain_dict = dict()                     # 딕셔너리로 구성
for i in range(10):                      # 10개 값을 입력 받을 것
    num = int(input())
    remain_num = num % 42                # 42로 나눈 나머지를 할당
    if remain_num not in remain_dict:    # 딕셔너리 안에 없다면 key 값을 추가하고 그 value를 1로 할당
        remain_dict[remain_num] = 1
    else:
        # remain_dict[remain_num] += 1     # 있다면 해당 key 값의 value에 1씩 더해줌 (생각해보니 굳이 더해 줄 것도 없음)
        continue                           # 어차피 중복값은 제거하고 갯수를 구하는 것이므로

result = len(list(remain_dict.values())) # 결과 값은 이 value의 길이를 구하면 됨
print(result)
# 정답 72ms

# set을 이용한 풀이
remain = set()
for i in range(10):
    n = int(input())
    remains = n % 42
    remain.add(remains)

result = len(remain)
print(result)
# 정답 72ms
