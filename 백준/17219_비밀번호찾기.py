
N, M = map(int, input().split(' '))

dict = {}

for _ in range(N):
    address, pwd = input().split(' ')
    dict[address] = pwd


for _ in range(M):
    res = input()
    print(dict[res])
