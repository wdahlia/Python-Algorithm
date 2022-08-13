
import sys
sys.stdin = open('1764.txt')

# 듣지도 못한 사람의 수 N
# 보지도 못한 사람의 수 M
# 듣도 보도 못한 사람의 명단을 사전 순으로 출력

# 교집합 사용
N, M = map(int, input().split())

not_heard = set(input() for _ in range(N))
not_seen = set(input() for _ in range(M))

result_list = sorted(not_heard & not_seen)

print(len(result_list))
print(*result_list, sep='\n')

# 딕셔너리 사용
res = dict()

N, M = map(int, input().split())

for _ in range(N):
    not_heard = input()
    if not_heard not in res:
        res[not_heard] = 1

for _ in range(M):
    not_seen = input()
    if not_seen in res:
        res[not_seen] += 1
    else:
        continue

result = []
for key, value in res.items():
    if value >= 2:
        result.append(key)

result.sort()

print(len(result))
print(*result, sep = '\n')
        