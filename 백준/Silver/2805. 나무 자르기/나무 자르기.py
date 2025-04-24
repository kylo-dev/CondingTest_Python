import sys
input = sys.stdin.readline


# 적어도 M미터의 나무를 집에 가져가기 위한 "절단기의 높이 최댓값"
# 최소를 위한 최댓값

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 1
right = max(trees)
max_height = 0

while left <= right:
    mid = (left + right) // 2

    total = sum((tree - mid) for tree in trees if tree > mid)
    
    if total < M:
        right = mid - 1
    else:
        max_height = mid
        left = mid + 1

print(max_height)