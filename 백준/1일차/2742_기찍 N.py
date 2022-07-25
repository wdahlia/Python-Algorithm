# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

N = int(input())

# ==================== 1
for i in range(1, N+1):
    if (N+1)-i > 0:
        print((N+1)-i)

# ==================== 2
for i in range(N, 0, -1):
    print(i)