import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

res = [0] * 101
for i in range(3):
  a, b = map(int, input().split())

  for x in range(a, b):
    res[x] += 1

ans = 0
for i in range(len(res)):
  if res[i] > 0:
    ans += (res[i] * arr[res[i] - 1])

print(ans)