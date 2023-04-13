
N = int(input())
houseArray = [list((map(int, input().split(' ')))) for _ in range(N)]


for i in range(1, N):
  houseArray[i][0] += min(houseArray[i-1][1], houseArray[i-1][2])
  houseArray[i][1] += min(houseArray[i-1][0], houseArray[i-1][2])
  houseArray[i][2] += min(houseArray[i-1][0], houseArray[i-1][1])

print(min(houseArray[N-1]))
