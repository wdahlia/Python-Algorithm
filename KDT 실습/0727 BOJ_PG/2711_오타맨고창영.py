import sys
sys.stdin = open('오타맨고창영.txt')


T = int(input())

# 방법1 - 리스트로 만든다음 해당 인덱스를 pop한 다음 join해서 출력하는 법
for _ in range(T):
    idx, typo = input().split()
    idx = int(idx)
    result = list(typo)
    result.pop(idx-1)
    print(''.join(result))

# 방법2 - 문자열에 주어진 인덱스와 같지 않은 문자열을 더해가는 방법
for _ in range(T):
    idx, typo = input().split()
    idx = int(idx)
    result = ''
    for i in range(len(typo)):
        if i == idx-1:
            pass
        else:
            result += typo[i]
    print(result)

# 방법3 - 슬라이싱 이용해 출력하는 방법
for _ in range(T):
    idx, typo = input().split()
    idx = int(idx)
    print(typo[:idx-1], end ='')
    print(typo[idx:])

