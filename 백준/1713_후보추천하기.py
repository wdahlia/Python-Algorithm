
import sys
sys.stdin = open('1713.txt')

from collections import deque

# 추천 시작 전에 모든 사진틀은 비어있다
# 특정 학생을 추천, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 함
# 비어있는 틀 없다면 현재까지 추천 받은 횟수가 가장 적은 학생의 사진 삭제, 새롭게 추천받은 학생의 사진 게시
# 가장 적은 학생이 두명 이상인 경우 가장 오래된 사진을 삭제
# 게시된 사진인데 다른 학생이 추천을 했다면 추천받은 횟수만 증가
# 사진틀에 게시된 사진이 삭제되는 경우 추천받은 횟수는 0으로 바뀜

N = int(input())
recommendNum = int(input())
studentsNum = list(map(int, input().split()))

# 뭔가 람다식을 쓸수 있을 것 같은 느낌..벗 어케 써야할지 모르겠삼
# 그리고 dict 쓰기

pic_list = []
pic_dict = {}
for i in studentsNum:
    if len(pic_dict) < N:
        if not pic_dict.get(i):
            pic_list.append(i)
        pic_dict[i] = pic_dict.get(i, 0) + 1 # cnt 해주는 것

    else:
        if i in pic_list:
            pic_dict[i] += 1

        else:
            min_num = min(pic_dict.values())
            for k, v in pic_dict.items():
                if v == min_num:
                    del(pic_dict[k])
                    num_idx = pic_list.index(k)
                    pic_list.pop(num_idx)
                    pic_list.insert(num_idx, i)
                    pic_dict[i] = pic_dict.get(i, 0) + 1
                    break

pic_list.sort()
print(*pic_list)
    
                    
                    

    