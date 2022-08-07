import sys
sys.stdin = open('셀프넘버.txt')

# d(n)은 n과 n의 각 요소를 돌면서 더한 값을 더해주는 것
# n은 d(n)의 생성자 즉 1은 2의 생성자 1+1 = 2
# 나는 생성자가 없는 애들 즉 생성자 없는 d(n)을 한 줄씩 출력해주어야 함

# 딕셔너리를 이용해서 풀이
dict_dn = {} 
for dn in range(1, 10000): # 1부터 10000까지의 숫자를
    dict_dn[dn] = 0 # 키에 넣고 value는 전부 다 0으로 초기화 해준다

for dn in range(1, 10000): # 다시 1부터 10000까지 돌면서
    dn1 = str(dn) # 문자열로 바꿔준다, for문에서 각 자리수를 더해주기 위함
    sum_n = 0 # dn이 바뀔때마다 다시 sum을 해줄 것이기에 0으로 초기화
    for i in range(len(dn1)):
        sum_n += int(dn1[i]) # 각 자리수를 sum_n에 더해줍니다
    sum_n += dn # 그리고 마지막으로 sum_n에 dn을 더해줌

    if sum_n in dict_dn: # 그 값이 딕셔너리에 있는 경우 (무조건 존재)
        dict_dn[sum_n] += 1 # value에 1을 더해준다

for key, value in dict_dn.items(): # key,value들을 모두 순환하면서
    if value == 0: # value값이 0인 애들의
        print(key) # key값을 뽑아줘라
