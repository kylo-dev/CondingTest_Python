import sys
import math

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
  arr = list(map(int, input().split()))
  total = 0
  
  for i in range(1, len(arr)):
    for j in range(i+1, len(arr)):
      total += math.gcd(arr[i], arr[j])

  print(total)