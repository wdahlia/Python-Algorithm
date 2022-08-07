

# word 주어질때 
# dictionary 활용
# 해당 문자열에서 등장한 모든 알파벳 갯수 구해 출력

word = input()
dict = {}
for str in word:
    if str not in dict:
        dict[str] = 1
    else:
        dict[str] += 1
    

for x, y in dict.items():
    print (x, y)

    