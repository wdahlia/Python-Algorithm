
# 방법 1
A, B = map(int, input().split())

list_ = []
for i in range(1, B+1):
    if i:
        list_ += [i] * i

print(sum(list_[A-1 : B]))
# 정답 76ms 

# 방법 2
arr = []
N = 1
while len(arr) < B:
    for _ in range(N):
        arr.append(N)
    N += 1

print(sum(arr[A-1 : B]))
