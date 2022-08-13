
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# n을 사용하지 않고 코드를 짜는 방법도 있으나
# 문제에서 우선 주어졌으므로 최대한 활용해서 짜본다

# ================================= n 사용
n, x = map(int, input().split())

A = list(map(int, input().split()))

for i in range(n):
    if A[i] < x:
        print(A[i], end=' ')

# ================================= n 사용 X
n, x = map(int, input().split())

A = list(map(int, input().split()))

for i in A:
    if i < x:
        print(i, end=' ')
        