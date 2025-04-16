import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
check = list(arr)

cnt = 0

for num in arr:
    if num in check and M - num in check and num != M - num:
        check.remove(num)
        check.remove(M - num)
        cnt += 1

print(cnt)