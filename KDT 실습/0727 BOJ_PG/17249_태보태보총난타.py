import sys
sys.stdin = open('태보태보총난타.txt')

taebo = input().split('(^0^)') # 얼굴을 기준으로 인풋값을 나눠서 받아준다

for char in taebo: 
    result = char.count('@') 
    # 결국 주먹의 잔상이 = 로 시작하여 @로 끝난다는것은 @가 펀치의 끝이므로 이 개수를 세면
    # 그 값이 결국 답이 된다는 것
    print(result, end = ' ')