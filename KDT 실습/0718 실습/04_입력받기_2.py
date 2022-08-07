
# 오류코드 
'''
words = list(map(int, input().split()))
print(words)
'''
# input : I'm Tutor 6
# output : ["I'm", 'Tutor', '6']

# 맵은 적어도 두개의 arugment가 있어야함.
# 한 문장 안의 띄어쓰기 된 부분으로 분해하고 싶다면
# 그냥 input().split()으로 코드 완성하면 됨
# words = list(map(int, input().split()))
# print(words)

words = input().split()
print(words)
