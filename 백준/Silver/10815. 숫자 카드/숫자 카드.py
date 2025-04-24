import sys
input = sys.stdin.readline
import bisect

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 가지고 있는지 확인할 카드
M = int(input())
check_list = list(map(int, input().split()))

for check in check_list:
    idx = bisect.bisect_left(arr, check)

    if idx < len(arr) and arr[idx] == check:
        print(1, end=" ")
    else:
        print(0, end=" ")