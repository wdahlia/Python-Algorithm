
N = int(input())

c_list = [] # 생성자리스트(constructor list)
for i in range(1, N+1):
    # i를 문자열로 변환하여 순환한 후 int로 변환해서 그것들을 더한다 - map, sum 사용
    # for문 안에 for문 넣는 방법은 이중 for문 이라 시간 많이 소요될 듯
    sum_n = sum(map(int, str(i)))
    d = i + sum_n # 분해합인 decomposition의 약자인 d에 더한 값을 할당
    if d == N:
        c_list.append(i)
        # 나는 이렇게 풀었지만 개인적으로는
        # if d == N:
        # print(i)
        # break # 왜냐면 min값을 프린트하라고 했기 때문에 1 ~ N까지 순회이므로 최소값인 생성자는
                # 처음 N과 일치하게 된 d값 일 것
        # if i == N: # 만약 생성자 없이 나랑 만나게 된다면, 그건 생성자 없는 것
        # print(0)

# 그냥 for-else 사용하는 방법도 존재 break 만나지 않는다면 else 실
# else:
# print(0)

# 문제를 잘 안읽어봤더니 런타임에러가 남
# 자연수 N의 생성자가 없을 수도 있음 즉, 리스트의 길이가 0인 경우는 print(0)
if len(c_list) == 0:
    result = 0
else:
    result = min(c_list)
# else에 그 외의 나머지의 경우는 min값을 찾아 result에 할당하고
# print 한다
print(result)
