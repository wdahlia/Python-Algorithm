
import sys
sys.stdin = open('2776.txt')

T = int(input())

for _ in range(T):

    n1 = int(input())
    note_n1 = set(map(int, input().split()))
    
    n2 = int(input())
    note_n2 = list(map(int, input().split()))

    for note in note_n2:
        if note in note_n1:
            print(1)
        else:
            print(0)
