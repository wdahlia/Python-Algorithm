
# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 리스트의 득표수 구하는 법
# 내가 이름을 입력했을 때 리스트 함수 내부에 있다면 반복문을 통해 내가 입력한것과 순환시 출력되는 값의 일치가
# 일어날 때, count에 1을 더해주자
# 이영희, 조민지, 김철수 모두에게 적용 

name = input()
cnt = 0
for str in students:
    if name == str:
        cnt += 1
print(cnt)