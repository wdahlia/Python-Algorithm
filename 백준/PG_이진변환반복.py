
def solution(s):
    
    result = []
    zero = num = cnt = 0
    while len(s) != 1:

        zero = s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')

        cnt += zero
        num += 1

    result.append(num)
    result.append(cnt)

    return result
        