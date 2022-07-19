

# 20번이랑 연결지어서 생각하면 매우 간편
# 10으로 나누었을때 그 나머지를 기록한다 생각하면된다!
# 그 결과값을 end=''해서 출력하는 방식으로 접근

number = int(input())
r = 0

while number != 0: # > 사용해도 무방
    r = number % 10
    a = []
    number //= 10
    print(r, end='')

