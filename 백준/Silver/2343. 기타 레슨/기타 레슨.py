import sys

input = sys.stdin.readline

# N: 강의 수, M: 블루레이 개수
N, M = map(int, input().split())

classes = list(map(int, input().split()))

left, right = max(classes), sum(classes)
answer = right

while left <= right:
    mid = (left + right) // 2

    count = 1
    sum_time = 0

    for class_time in classes:
        if sum_time + class_time > mid:
            sum_time = class_time
            count += 1
        else:
            sum_time += class_time
    
    if count > M:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
