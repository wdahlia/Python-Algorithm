
import sys
sys.stdin = open('2309.txt')

n = 9
dwarf = []
for _ in range(n):
    height = int(input())
    dwarf.append(height)

dwarf_h = sorted(dwarf)
sum_h = sum(dwarf_h)

for i in range(n):
    for j in range(i+1, n):
        if sum_h - (dwarf_h[i] + dwarf_h[j]) == 100:
            for k in range(n):
                if k != i and k != j:
                    print(dwarf_h[k]) 


