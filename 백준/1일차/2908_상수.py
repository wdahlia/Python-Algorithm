
# ================ 슬라이싱 사용 

# n_1과 n_2를 한 칸 공백을 기준으로 나누어 출력 (type : str)
n_1, n_2 = input().split()
# 슬라이싱 역순으로 한 다음 n_1, n_2 int로 변환 (type : int)
n_1 = int(n_1[::-1])
n_2 = int(n_2[::-1])

# n_1이 크다면 n_1 출력, 아니라면 n_2 출력

if n_1 > n_2:
    print(n_1)
else:
    print(n_2)
