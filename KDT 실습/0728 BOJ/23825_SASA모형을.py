# 결국 문제는 어렵게 표현했지만
# 모형 1개 만들떈 S모양 블록 2개 and A모양 2개가 필요하다는 것 잊지말자
# 즉, input 받은 값 중 작은 값을 2로 나눈 몫인 것

NM = list(map(int, input().split())) # 띄어쓰기를 기준으로 input() 받은 값을 int로 형변환 해서 리스트에 저장

NM = min(NM) # 리스트 중 min값을 찾아줘!


result = NM // 2 # 2로 나눠줘

print(result)

# 68ms
