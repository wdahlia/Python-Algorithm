
def solution(price, money, count):
    # N번 째 이용한다면 원래 이용료의 N배를 받기로함
    # count번 타게 된다면 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return
    # 금액 부족하지 않다면 0을 return

    while count:
        value = price * count
        money -= value
        count -= 1
    
    if money >= 0:
        return 0
    else:
        return abs(money)
        