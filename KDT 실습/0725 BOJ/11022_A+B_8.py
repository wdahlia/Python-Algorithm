
T = int(input())

for n in range(1, T+1):
    a, b = input().split()
    result = int(a) + int(b)
    print(f'Case #{n}: {a} + {b} = {result}')
