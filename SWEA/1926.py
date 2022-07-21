import sys
sys.stdin = open('1926.txt', 'r')

n = int(input())
for i in range(1, n+1):
    i = str(i)
    cnt = 0
    for num in i:
        if num in '369':
            cnt += 1
    if cnt == 0:
        print(i,end=' ')
    else:
        print('-' * cnt,end=' ')
    

    
