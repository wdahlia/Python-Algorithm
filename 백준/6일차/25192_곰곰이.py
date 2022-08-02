import sys
sys.stdin = open('25192_곰곰이.txt')


T = int(input())

cnt = 0
user_set = set()
for _ in range(T):
    user_name = input()

    if user_name == 'ENTER':
        n = len(user_set)
        cnt += n
        user_set = set()
        
    else:
        user_set.add(user_name)

print(len(user_set) + cnt)

# 4044ms


cnt = 0
user_set = set()
for _ in range(T):
    user_name = input()

    if user_name == 'ENTER':
        user_set = set()
    else:
        if user_name not in user_set:
            user_set.add(user_name)
            cnt += 1
print(cnt)
