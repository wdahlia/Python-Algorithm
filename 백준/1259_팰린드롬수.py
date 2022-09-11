
import sys
sys.stdin = open('1259.txt')

# 뒤에서부터 읽어도 똑같다면 팰린드롬이라고 함

number = input()
while number != '0':
    if number == number[::-1]:
        print('yes')
    else:
        print('no')  
    number = input()  


number = input()
while number != '0':
    result = 'yes'
    for idx in range(len(number)//2):
        if number[idx] == number[-(idx+1)]:
            continue
        else:
            result = 'no'
            break

    print(result) 
    number = input()  