
# 'Quadrant n은 '제n사분면'이라는 뜻이다.
# x > 0, y > 0 이면 1
# x > 0, y < 0 이면 4
# x < 0, y > 0 이면 2
# x < 0, y < 0 이면 3


x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
        