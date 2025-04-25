import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right, total = 0, 0, 0
min_len = 10e6

while True:
    if total >= S:
        min_len = min(min_len, right - left)
        total -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        total += arr[right]
        right += 1

if min_len == 10e6:
    print(0)
else:
    print(min_len)