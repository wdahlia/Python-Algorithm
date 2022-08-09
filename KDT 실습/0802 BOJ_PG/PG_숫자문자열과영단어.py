
def solution(s):

    
    en_dict = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }

    for key, value in en_dict.items():
        if key in s:
            s = s.replace(key, str(value))
    
    result = int(s)
    return result

s = 'one4seveneight'
print(solution(s))
