
import sys
sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for _ in range(1, T+1):

    num_dict = {}                            # 빈 딕셔너리를 만들어준다

    T_n = int(input()) 

    number = list(map(int, input().split())) # 공백을 기준으로 값을 출력하여 list로 넣어줌

    for n in number:
        if n not in num_dict:                # 순회할때 n이 dict에 없다면
            num_dict[n] = 1                  # n을 key에 저장 초기값 1을 value에 저장
        else:
            num_dict[n] += 1                 # n이 dict에 있다면 그 키값에 1을 더해준다

    result_list = []                         # 빈 리스트를 생성
    m = max(num_dict.values())               # 코드 수정 m의 변수에 max값을 저장하고
    for key, value in num_dict.items():      # 딕셔너리 key value를 순회하면서
        if m == value: # 코드 수정
                                             # 이전 코드 - if max(num_dict.values()) == value: 
                                             # 이전 코드 - max값은 변화하지 않는데 계속 for문 돌면서 계속해서 max값 계산 시간 많이 걸림
            result = key                     # 그 해당 key를 뽑아내서 result에 저장
            result_list.append(result)       # 빈리스트에 그 키를 저장해준다
            if len(result_list) == 2:        # 만약 모두 저장된 리스트의 길이가 2이면 즉, 중복값이 있다면
                result = max(result_list)    # 그중 가장 큰 값을 최종 result에 다시 할당

    print(f'#{T_n} {result}') 

# 런타임에러가 남 이유는 중복값 중 큰값을 최종 result에 넣어야 한다는 조건을 추가하지 못했기 때문
# 보완해 주신 부분을 추가
