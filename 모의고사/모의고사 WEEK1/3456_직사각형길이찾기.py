import sys
sys.stdin = open('직사각형길이찾기.txt')

T = int(input())

for i in range(1, T+1):
    case = list(map(int, input().split())) # 빈칸을 기준으로 input값을 리스트에 저장

    max_n = max(case) # case 중 max 값을 찾는다
    min_n = min(case) # case 중 min 값을 찾는다

    if case.count(max_n) == 2: # 만약 max값을 카운트 한 것이 리스트에 2개라면
        print(f'#{i} {min_n}') # min 값을 출력해주고
    elif case.count(min_n) >= 2: # 만약 min값과 같은 것이 리스트에 2개 이상이라면 (2,2,3 이라던지 2,2,2의 경우)
        print(f'#{i} {max_n}') # max 값을 출력해줍니다 > 전부다 2,2,2인경우는 어차피 max값도 2이기 때문에 상관 없음



    

    

