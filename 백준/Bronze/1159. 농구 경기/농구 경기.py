import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
player = {}
for i in range(n):
  p = input().rstrip()[0]
  if p in player:
    player[p] += 1
  else:
    player[p] = 1

ans = []
for key, value in player.items():
  if value >= 5:
    ans.append(key)

ans.sort()
if not len(ans):
  print("PREDAJA")
else:
  print("".join(ans))
