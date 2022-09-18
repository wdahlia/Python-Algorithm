
import sys
sys.stdin = open('13458.txt')

# N개의 시험장, i번 시험장에 있는 응시자의 수는 Ai명
# 총감독관, 부감독관
# 총 - B명
# 부 - C명
# 총은 1명, 부감은 여러명 가능
# 필요한 감독관 수 최솟값을 구하시오

N = int(input())
applicant = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    remainder = applicant[i] - B
    if remainder > 0:
        subNum = remainder // C
        if remainder % C > 0:
            result += subNum + 1
        else:
            result += subNum

    result += 1
        
print(result)
