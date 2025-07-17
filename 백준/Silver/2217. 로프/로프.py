import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

answer = 0
arr.sort()

for i in range(N):
    cnt = N - i
    answer = max(answer, cnt * arr[i])

print(answer)