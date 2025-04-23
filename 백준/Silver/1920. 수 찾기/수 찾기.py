import sys
input = sys.stdin.readline
import bisect

M = int(input())
arr = list(map(int, input().split()))
arr.sort()

N = int(input())
check_list = list(map(int, input().split()))

def is_exist(arr, check):
    idx = bisect.bisect_left(arr, check)

    if idx < len(arr) and arr[idx] == check:
        return 1
    return 0


for check in check_list:
    print(is_exist(arr, check))