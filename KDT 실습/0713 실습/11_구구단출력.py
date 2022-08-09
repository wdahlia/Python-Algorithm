
# 구구단을 출력

for x in range(2, 10):
    print(x,'단',sep='')
    for y in range(1, 10):
        print(f'{x} X {y} = {x * y}')
        