
import sys
sys.stdin = open('23253.txt')


N, M = list(map(int, input().split()))
result = []
for i in range(M):
    n = int(input())
    books_n = list(map(int, input().split()))
    

    while len(books_n) > 1:
        compare_n = books_n.pop()
        if compare_n > books_n[-1]:
            result.append('No')
            break

if 'No' in result:
    print('No')
else:
    if len(result) == 0:
        print('Yes')
        