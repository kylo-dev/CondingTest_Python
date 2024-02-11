n = int(input())
arr = list(map(int, input().split()))
time = 0
tol = 0
arr.sort()
for i in arr:
  time = time + i
  tol += time
print(tol)