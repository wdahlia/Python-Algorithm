
import sys
sys.stdin = open('6588.txt')

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있음을 검증하는 프로그램 작성
# 입력의 마지막 줄에 0이 하나 주어짐
# n = a + b 의 형태로 출력
# 만들 수 있는 방법이 여러 가지라면, b-a이 가장 큰 것을 출력
# n을 나타낼 수 없는 경우는 Goldbach's conjecture is wrong.을 출력

array = [True for _ in range(1000001)]

for i in range(2, 1001):
    if array[i] == True:
        j = 2
        while i * j <= 1000000:
            array[i * j] = False
            j += 1

switch = True
while switch:
    n = int(input())
    if n == 0:
        switch = False
    else:
        for k in range(3, 1000001):
            if k != 1 or n-k != 1:
                if array[k]:
                    if array[n-k]:
                        print(f'{n} = {k} + {n-k}')
                        break
                    
        else:
            print("Goldbach's conjecture is wrong.")
            
        

