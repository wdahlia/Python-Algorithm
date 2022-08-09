import sys
sys.stdin = open('암호문1.txt')

# 11개 이거는 리스트의 길이임
# 근데 I 뒤에 있는 x의 값은 인덱스임 그다음 y개의 숫자는 y개를 넣으라는 소린데
# 만약 y개를 다 채우지 못하고 다른 I 삽입문의 x 인덱스가 있는경우에는 그 삽입문의 암호를 넣어주는것

for i in range(1, 11):
    origin_len = int(input())
    origin_text = list(input().split())
    N = int(input())
    command_text = input().split()


    
    idx = 0 # 인덱스
    new = 0 # origin_text에 새로 추가 할 것
    cnt = 0 # idx 숫자에 더해 줄 것
    for r in range(len(command_text)):
        if command_text[r] == 'I': # r이 'I'와 같으면 I 뒤에 새로운 인덱스와 문자 갯수 주어짐으로 초기화
            new = 0
            cnt = 0
            idx = 0
        else: # r이 I와 같지 않을때 
            if command_text[r-1] == 'I': # origin_text에 insert 할 값은 I 뒤에 주어짐
                idx = command_text[r]
            elif command_text[r-2] == 'I': # origin_text에 추가할 문자열의 갯수는 I 2칸 뒤 주어짐
                pass # 이 경우를 pass한 이유는 else에서 갯수 상관 없이 모든 새로운 I앞의 문자열을 
                     # origin_text에 추가해줄 것이므로
            else: # idx값과 개수를 제외한 나머지 값들
                new = command_text[r] # 그 인덱스의 값을 origin_text에 insert하기 전에 new에 할당
                origin_text.insert(int(idx)+cnt, new) # idx를 int로 변환한 값에 cnt(초기에는 0)을 더한 인덱스에 new를 추가
                cnt += 1 # 1씩 더해준다. 새로운 I 튀어나오기 전까지

    origin_text = origin_text[:10] # 변환된 origin_text 값을 10개만 출력하라 했으므로 슬라이싱 해준다

    print(f'#{i}', end=' ') # f스트링을 사용하여 #{i} end를 한칸 공백으로하고 origin_text 즉 리스트를 * < 순환하며
    print(*origin_text) # 그 값을 #{i}와 공백을 두고 ' ' 출력
        

            

    

    



    
