import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

max_length = 0
left = 1
right = max(snacks)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for snack in snacks:
        cnt += snack // mid
    
    if cnt < M:
        right = mid - 1
    else:
        max_length = mid
        left = mid + 1

print(max_length)