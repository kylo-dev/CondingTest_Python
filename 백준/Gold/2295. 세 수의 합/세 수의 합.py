import sys
input = sys.stdin.readline

n = int(input())
u = set()

for i in range(n):
  u.add(int(input()))

ab_sums = set()

for i in u:
  for j in u:
    ab_sums.add(i+j)

ans = set()

for i in u:
  for j in u:
    if (i-j) in ab_sums:
      ans.add(i)

ans = sorted(list(ans), reverse=True)
print(ans[0])