n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 1
start = arr[0]

for i in arr:
  if i in range(start, start + l):
    continue

  cnt += 1
  start = i

print(cnt)