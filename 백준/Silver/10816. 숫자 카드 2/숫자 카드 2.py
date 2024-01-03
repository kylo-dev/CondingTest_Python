import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))

m = int(input())
cards = list(map(int, input().split()))

dict = {}

for i in nums:
  if i in dict:
    dict[i] += 1
  else:
    dict[i] = 1

def binary(arr, target, start, end):
  if (start > end):
    return 0
    
  mid = (start+end)// 2
  if arr[mid] == target:
    return dict.get(target)
  elif arr[mid] > target:
    return binary(arr, target, start, mid-1)
  else:
    return binary(arr, target, mid+1, end)
    
for i in cards:
  print(binary(nums, i, 0, n-1), end=" ")