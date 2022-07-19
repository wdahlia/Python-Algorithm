# import sys
# sys.stdin = open('2071.txt', 'r')

T = int(input())

for i in range(1, T+1):
    a = list(map(int, input().split()))
    if a:
        b = sum(a[::])/len(a)
        print(f'#{i} {round(b)}')


## sum 함수 안쓰고 for문으로 

for i in range(1, T+1):
    l = 0
    s = 0
    num = list(map(int, input().split()))
    for n in num:
        s += n
        l += 1
    result = s/l
    print(f'#{i} {round(result)}')
