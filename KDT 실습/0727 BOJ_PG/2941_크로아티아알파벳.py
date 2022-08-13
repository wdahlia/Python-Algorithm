
word = input()

croatia_alph = ['c=' , 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alph in croatia_alph:
    word = word.replace(alph, '_')

print(len(word))

# 내장함수인 replace를 활용하면 금방 풀리는 문제
# 중복인 알파벳은 숫자계산에서 뺀다던지 하는게 없기 때문에 금방 풀림
