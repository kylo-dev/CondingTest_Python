import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

sorted_nums = sorted(set(nums))

dict = {sorted_nums[i]: i for i in range(len(sorted_nums))}

for i in nums:
  print(dict[i], end=" ")