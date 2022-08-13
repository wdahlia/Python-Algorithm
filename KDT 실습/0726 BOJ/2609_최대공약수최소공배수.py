
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 한 칸 띄운 것을 기준으로 input() 받은것을 나누어 int로 변환 후 n1, n2에 할당
n1, n2 = map(int, input().split())

# 최대공약수를 먼저 구해야한다. 즉, list로 append해서 두 리스트에서 공통 인자를 뽑아내야함 
# > 이중 for문 될듯

def gcf_lcm():
    n1_list = []
    n2_list = []

    for i in range(1, n1+1):
        if n1 % i == 0: # n1을 i로 나누었을때 0
            n1_list.append(i)

    for j in range(1, n2+1):
        if n2 % j == 0:
            n2_list.append(j)

    result_li = []
    for n1_li in n1_list:
        for n2_li in n2_list:
            if n1_li == n2_li:
                result_li.append(n1_li)

    gcf = max(result_li)
    
    print(gcf)

    # 이어서 최소 공배수 구하는 법 - 각 input한 n1 n2를 최대공약수로 나눈 후 최대공약수와 곱해줌
    n1_ = n1 // gcf
    n2_ = n2 // gcf

    lcm = gcf * n1_ * n2_ 

    print(lcm)

gcf_lcm()
