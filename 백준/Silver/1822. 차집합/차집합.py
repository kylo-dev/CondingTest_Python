import sys
input = sys.stdin.readline

A, B = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

answer = set(a_list) - set(b_list)

answer = sorted(list(answer))
print(len(answer))

for i in answer:
    print(i, end=" ")
