
import sys
sys.stdin = open('6190.txt')

# 각 숫자의 자릿수가 단순하게 증가하는 수를 의미
def switch(strNum):
    for k in range(len(strNum)-1):
        if strNum[k] > strNum[k+1]:
            return False
    return True
    
T = int(input())

for idx in range(1, T+1):
    N = int(input())
    numList = list(map(int, input().split()))

    maxNum = 0
    for i in range(N-1):
        for j in range(i+1, N):
            newNum = numList[i] * numList[j]
            strNum = str(newNum)
            if switch(strNum):
                maxNum = max(maxNum, newNum)            
  
    if maxNum == 0:
        maxNum = -1

    print(f'#{idx} {maxNum}')
