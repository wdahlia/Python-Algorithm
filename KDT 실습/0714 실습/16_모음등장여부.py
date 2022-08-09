
word = input()
m = ['a', 'e', 'i', 'o', 'u']
n = 0
for str in word:
    if str in m:
        n += 1
print(n)

# 굳이 리스트로 안만들고 str in 'aeiou' 해도 됨
