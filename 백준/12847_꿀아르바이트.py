
import sys
sys.stdin = open('12847.txt')

# n일 후까지 일급 정보를 알아냈다. 최대 m일 밖에 일을 할 수 없다
# 최대이익의 값을 원하는 것
# 즉, 연속된 일수의 합계가 중요한 포인트
# 나는 m일 연속해서 일을 할 수 밖에 없으니
# 조건에 보면 일을 시작한 날부터 끝날 때까지 하루도 빠지면 안된다고함
# 같은 면적의 값들을 알아내는 방법인, 슬라이딩 윈도우 알고리즘을 사용해야 함
# 시간 복잡도를 부분 배열을 활용하여 O(N)으로 감소 가능
# 즉 start가 한칸씩 이동을 하는데, 이동할때마다 그 전값은 빠져도 됨

# 누적합
N, M = map(int, input().split())
salaryList = list(map(int, input().split()))
sumSalary = [0] * (N+1)
sumNum = result = 0
for i in range(N):
    sumNum += salaryList[i]
    sumSalary[i+1] = sumNum
    
for j in range(N-M):
    compareNum = sumSalary[j+M] - sumSalary[j]
    result = max(result, compareNum)

print(result)

# 슬라이딩 윈도우
# 처음의 sum 값을 저장
start = 0
end = M
sumNum = sum(salaryList[start:end])
maxSum = sumNum

while end < N:
    sumNum = sumNum + salaryList[end] - salaryList[start]
    maxSum = max(sumNum, maxSum)
    start += 1
    end += 1

print(maxSum)
