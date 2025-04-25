import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left, right, total = 0, 0, 0

while True:
    if total > M:
        total -= arr[left]
        left += 1
    elif total == M:
        answer += 1
        total -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        total += arr[right]
        right += 1

print(answer)