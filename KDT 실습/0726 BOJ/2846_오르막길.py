
# 순회 할 때, 각 인자의 값이 증가해야지 오르막길 즉, 부분 수열이 된다.
# 리스트를 만들어서 인덱스 끝과 처음을 빼볼까 생각했지만 시간 너무 많이 걸림
# 그래서 리스트 안을 순환하면서 인덱스와 그 다음인덱스의 차가 음수인 경우
# 그 다음 인덱스의 차와 전 인덱스의 차 값을 dif에 더해간다면 오르막길인 부분 수열의 맨 처음과 끝을 빼는 값과 같아짐
# 그리고 이 값을 dif_list=[]라는 곳에 저장한다.

T = int(input()) # 수열의 크기 즉 수열의 길이 - 입력

arr = list(map(int, input().split())) # 수열 안에 들어가는 Tㄱ

dif = 0 # 차이값
dif_list = []
for i in range(T-1): # out of range 해결
    if arr[i] - arr[i+1] < 0:
        dif += arr[i+1] - arr[i]
        dif_list.append(dif)
    if arr[i] - arr[i+1] >= 0: # 만약 인덱스와 다음인덱스의 차가 같거나 양수라면 - 값이 줄어들고 있거나 똑같다는 것
        dif = 0 # 그 경우 dif를 초기화해줘야함


if len(dif_list) == 0: # 만약 dif list에 어떠한 값도 추가되지 못한다
    result = 0 # 0을 반환
else:
    result = max(dif_list) # 아니라면 dif_list중 가장 큰 값 반환해라

print(result)
