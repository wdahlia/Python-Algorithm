
import sys
sys.stdin = open('2309.txt')

# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다
# 아무거나 출력해도 상관이 없으므로 
n = 9
result = []
dwarf = []
for _ in range(n):
    height = int(input())
    dwarf.append(height)

dwarf_h = sorted(dwarf)
sum_h = sum(dwarf_h)

for i in range(n):
    for j in range(i+1, n):
        if sum_h - (dwarf_h[i] + dwarf_h[j]) == 100:
            result.append(dwarf_h[i])
            result.append(dwarf_h[j])
            break
    if len(result) == 2:
        break

k = len(result)

for idx in range(k):
    dwarf_h.remove(result[idx])

print(*dwarf_h, sep='\n')
