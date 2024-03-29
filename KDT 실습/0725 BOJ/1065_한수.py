
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# 즉,10은 1과 0으로 이루어짐 1-0=1 차이가 1인 등차수열
# 200은 2 0 0 2-0=2 0-0=0 2!=0 즉, 등차 수열이 아니다
# 로직은 간단하다 1의자리 숫자는 숫자 하나이므로 전부 다 등차수열
# 10의 자리 수들도 각 자리가 숫자 두개이므로 전부 다 등차수열
# 100 미만은 등차수열이다.
# 100 이상의 경우 문자열로 바꿔준 다음 인덱스로 접근해서 각 자리 숫자의 차가 같은지를 비교하면 될 듯
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

X = int(input())

cnt = 0
for i in range(1, X+1):
    if i < 100:
        cnt += 1
    else:
        i = list(map(int, str(i))) # str[i]를 순환하면서 int로 변환하고 그걸 list에 담는다
        if i[0] - i[1] == i[1] - i[2]:
            cnt += 1
print(cnt)
    