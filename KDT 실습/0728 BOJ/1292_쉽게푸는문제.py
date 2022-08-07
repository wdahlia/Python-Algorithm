ab_range = list(map(int, input().split()))

A = ab_range[0]
B = ab_range[1]

list_ = []
for i in range(1, B+1):
    if i:
        list_ += [i] * i

print(sum(list_[A-1 : B]))

# 정답 76ms 

# 밑의 방법은 오류
# 문자열이라서 50 53 이렇게 넘어가면 5, 0, 5, 3 이렇게 인식해서 더하는 것



ab_range = list(map(int, input().split()))

arr = []
N = 1
while len(arr) < B:
    for _ in range(N):
        arr.append(N)
    
    N += 1

print(sum(list_[A-1 : B]))


# for과 while을 전부 다 사용해서 문제 푸는 법 계속 연습