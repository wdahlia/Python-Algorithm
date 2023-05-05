
import sys
sys.stdin = open('7490.txt')

# ASCII 순서에 따라 결과가 0이 되는 수식 출력
# +, -, '' 공백은 수를 이어붙이는것
# eval 쓰면 

def dfs(num, result):
    global N
    if num == N:
        res = result.replace(' ', '')
        if eval(res) == 0:
            print(result)
        return
    
    if num < N:
        dfs(num + 1, result + ' ' + str(num + 1))
        dfs(num + 1, result + '+' + str(num + 1))
        dfs(num + 1, result + '-' + str(num + 1))
        # 덧셈인지 뺄셈인지 알려줘서 걔랑 값을 더해줘야됨
   
    
    
    
T = int(input())

for _ in range(T):
    N = int(input())
    dfs(1, '1')
    print()


