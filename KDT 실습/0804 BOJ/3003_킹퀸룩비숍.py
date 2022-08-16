
import sys
sys.stdin = open('3003.txt')

chess = [1, 1, 2, 2, 2, 8]
chess_n = list(map(int, input().split()))

for i in range(6):
    if chess[i] != chess_n[i]:
        chess[i] = chess[i] - chess_n[i]
    else:
        chess[i] = 0

print(*chess, sep=' ')
