
import sys
sys.stdin = open('1244.txt')

# 1은 스위치 on
# 0은 스위치 off
# 학생에게 1 이상이고 스위치 개수 이하인 자연수를 나누어줌
# 남 - 스위치 번호 자기가 받은 수의 배수 > 스위치의 상태를 바꾼다
# 여 - 자기가 받은 수와 같은 번호가 붙은 스위치 중심 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간 모두 바꾼다
# 스위치의 개수는 홀수

# 1
N = int(input())
switch = [-1] + list(map(int, input().split()))
studentnum = int(input())

for _ in range(studentnum):
    gender, num = map(int, input().split())

    if gender == 1:
        newnum = num
        while newnum <= N:
            if switch[newnum] == 1:
                switch[newnum] = 0
            else:
                switch[newnum] = 1
            newnum += num
    
    else:
        if switch[num] == 1:
            switch[num] = 0
        else:
            switch[num] = 1

        minus = num - 1
        plus = num + 1
        while True:

            if 0 <= minus and plus <= N:
                if switch[minus] == switch[plus]:
                    if switch[minus] == 1:
                        switch[minus] = 0
                        switch[plus] = 0
                    else:
                        switch[minus] = 1
                        switch[plus] = 1
                else:
                    break 
            else:
                break

            minus -= 1
            plus += 1

for i in range(1, N, 20):
    print(*switch[i:i+20])



#2
N = int(input())
switch = [-1] + list(map(int, input().split()))
studentnum = int(input())

for _ in range(studentnum):
    gender, num = map(int, input().split())

    if gender == 1:
        for idx in range(num, N+1, num):
            if switch[idx] == 1:
                switch[idx] = 0
            else:
                switch[idx] = 1
    
    else:
        if switch[num] == 1:
            switch[num] = 0
        else:
            switch[num] = 1

        minus = num - 1
        plus = num + 1
        while True:

            if 0 <= minus and plus <= N:
                if switch[minus] == switch[plus]:
                    if switch[minus] == 1:
                        switch[minus] = 0
                        switch[plus] = 0
                    else:
                        switch[minus] = 1
                        switch[plus] = 1
                else:
                    break 
            else:
                break

            minus -= 1
            plus += 1

for i in range(1, N, 20):
    print(*switch[i:i+20])
