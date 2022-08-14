
import sys
sys.stdin = open('1076.txt')

# 색 3개 이용 저항 몇 옴?
# yellow violet red 4 7 100 즉 4700

N = 3

# 색깔 리스트 생성
colors = ['black', 'brown', 'red', 'orange', 'yellow', 
'green', 'blue', 'violet', 'grey', 'white']    

result = []
for _ in range(N):
    color = input()                
    for idx in range(10):                  # input 받은 값이   
        if colors[idx] == color:           # colors[i]와 같다면
            result.append((idx, 10**idx))  # 튜플 형태로 result 리스트에 추가

res = ''                                   # 빈 문자열 생성
for i in range(N):
    if i == 0 or i == 1:                   # 첫 번째, 두 번째 일때는 
        res += str(result[i][0])           # 튜플 안의 첫번째 인덱스 값을 str 변환 후 더해주고
    else:                                  # 세 번째 인덱스일 때는
        res = int(res) * result[i][1]      # res값을 int로 변환한다음 튜플의 두번째 값을 곱해준다

print(res)
