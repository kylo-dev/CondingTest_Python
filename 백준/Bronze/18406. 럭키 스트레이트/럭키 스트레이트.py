import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
mid = len(n) // 2

left = sum(n[:mid])
right = sum(n[mid:])

if left == right:
  print("LUCKY")
else:
  print("READY")