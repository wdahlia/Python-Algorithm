
# 오류코드
'''
numbers = input().split()
print(sum(numbers))
'''
# input : 10 20
# output : 30

# 처음 상태는 리스트로 출력됨 리스트는 int로 변환 못함, 이때 사용하는 것이 map
# numbers = input().split()
# print(sum(numbers))

numbers = map(int, input().split())
print(sum(numbers))
