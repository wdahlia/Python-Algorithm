
import sys
sys.stdin = open('1302.txt')

# 책의 개수 N
# 책의 제목들, 소문자로만 이루어짐
# 가장 많이 팔린 책의 제목 출력
# 여러개일 경우 사전 순으로
# 가장 앞서는 제목만 출력하면 됨

books = dict()

N = int(input())

for _ in range(N):
    b_name = input()
    if b_name not in books:
        books[b_name] = 1
    else:
        books[b_name] += 1

max_ = max(books.values())
result = sorted(books.items())

for key in result:
    if key[1] == max_:
        print(key[0])
        break
    