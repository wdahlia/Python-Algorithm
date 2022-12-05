
import sys
sys.stdin = open('17388.txt')

# 참여도의 합 100이상 일처리 O
# 100미만 참여도가 가장 낮은 대학 동아리에 압박
# S, K, H
# 일처리 잘되면 OK

S, K, H = map(int, input().split())

univScore = [S, K, H]

if sum(univScore) >= 100:
    print('OK')

else:
    if min(univScore) == S:
        print('Soongsil')
    elif min(univScore) == K:
        print('Korea')
    else:
        print('Hanyang')
