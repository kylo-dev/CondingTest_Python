import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = []
total = float('inf')

start, end = 0, N - 1

while start < end:
    mid = arr[start] + arr[end]

    if abs(mid) < total:
        total = abs(mid)
        answer = [arr[start], arr[end]]

    if mid > 0:
        end -= 1
    elif mid < 0:
        start += 1
    else:
        break
print(' '.join(map(str, answer)))
