
import sys
sys.stdin = open('1526.txt')

# 금민수는 4, 7로만 이루어진 수를 말함
# N보다 작거나 같은 금민수중 가장 큰 것을 출력하는 프로그램

N = int(input())

while N >= 4: # n은 4보다 크거나 같다고 했으므로 4보다 작아질 경우 종료하게끔 설정
    cnt = 0 # cnt
    for i in str(N): # N을 문자열로 바꾼다음 순회
        if i == '4' or i == '7': # 4, 7이 있다면
            cnt += 1 # cnt 1을 해준다
    if cnt == len(str(N)): # 문자열의 길이와 cnt가 일치하면
        print(N) # N을 프린트해주고
        break # 브레이크
    else: # 다르다면
        N -= 1 # N에서 1빼준다
