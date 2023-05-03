
import sys
sys.stdin = open('14888.txt')

# 수의 개수 N
# N 만큼의 개수
# + - x /

def calculate(idx, pl, mn, mt, div, compare_num):

    global min_num, max_num
    
    if idx == N:
        min_num = min(min_num, compare_num)
        max_num = max(max_num, compare_num)
        return

    if pl > 0:
        calculate(idx + 1, pl - 1, mn, mt, div, compare_num + nums_array[idx])
    
    if mn > 0:
        calculate(idx + 1, pl, mn - 1, mt, div, compare_num - nums_array[idx])
    
    if mt > 0:
        calculate(idx + 1, pl, mn, mt - 1, div, compare_num * nums_array[idx])
        
    if div > 0:
        calculate(idx + 1, pl, mn, mt, div - 1, int(compare_num / nums_array[idx]))
    

N = int(input())
nums_array = list(map(int, input().split()))
p, m, mt, div = map(int, input().split())

min_num = 1e10
max_num = -1e10

calculate(1, p, m, mt, div, nums_array[0])  # 계산할 인덱스, 연산기호 값 줄이기위해서, 누적값

print(max_num)
print(min_num)