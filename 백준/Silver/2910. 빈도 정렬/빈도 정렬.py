import sys
from collections import Counter
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

arr_cnt = Counter(arr)

arr_cnt = sorted(arr_cnt.items(), key = lambda x: -x[1])

for key, value in arr_cnt:
  for _ in range(value):
    print(key, end=" ")
print()