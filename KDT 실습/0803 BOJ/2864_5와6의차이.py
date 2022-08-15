
import sys
sys.stdin = open('2864.txt')

# 5를 볼 때, 잘 볼때도 있지만, 6로 잘못 볼 수도 있고
# 6을 볼 때, 잘 볼때도 있지만, 5로 잘못 볼 수도 잇음
# 두 수의 가능한 합 중, 최소, 최대 구해 출력

# 즉, 5를 6로 볼때 최대값 
# 6을 5로 볼때 최소값임

# 방법 1
A, B = input().split()

max_num = int(A.replace('5', '6')) + int(B.replace('5', '6'))
min_num = int(A.replace('6', '5')) + int(B.replace('6', '5'))

print(min_num, max_num)
