import sys
input = sys.stdin.readline
from itertools import combinations

arr = []
for _ in range(9):
  arr.append(int(input().rstrip()))

for comb in combinations(arr, 7):
  if sum(comb) == 100:
    for i in sorted(comb):
      print(i)
    break
