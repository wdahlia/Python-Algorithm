
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# "a" or "e" or "i" or "o" or "u" 이런 식은 문자열 전부가 카운트 됨
# 차라리

word = "HappyHacking"

count = 0

for char in word:
    if (char == "a" or 
    char == "e" or 
    char == "i" or 
    char == "o" or 
    char == "u"):
        count += 1

print(count)

# or

word = "HappyHacking"

count = 0

for char in word:
    if char in 'aeiou':
        count += 1

print(count)