import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())
num = list(map(int, input().split()))

def binary_search(arr, start, end, n):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] > n:
      end = mid - 1
    elif arr[mid] < n:
      start = mid + 1
    elif arr[mid] == n:
      return True

for i in num:
  if binary_search(arr, 0, len(arr)-1, i):
    print(1)
  else:
    print(0)