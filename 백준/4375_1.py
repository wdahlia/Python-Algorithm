
import sys
sys.stdin = open('4375.txt')


def math(n):
    result = '1'
    while True:
        if int(result) % number == 0:
            return len(result)
        result += '1'


while True:
    try:
        number = int(input())
        print(math(number))
    except:
        break
