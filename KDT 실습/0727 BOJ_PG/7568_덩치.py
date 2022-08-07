N = int(input())

participant = []
for i in range(N):
    w, h = map(int, input().split())
    participant.append([w, h])


for part in participant:
    k = 1
    for part_ in participant:
        if part[0] < part_[0] and part[1] < part_[1]:
            k += 1
    print(k, end=' ')
