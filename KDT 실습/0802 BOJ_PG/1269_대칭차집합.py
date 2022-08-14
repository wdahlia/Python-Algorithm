
import sys
sys.stdin = open('1269.txt')

A, B = map(int, input().split())

a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

result = len(a_list - b_list) + len(b_list - a_list)
print(result)
