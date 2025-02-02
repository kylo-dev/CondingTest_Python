N = int(input())

arr = list(map(int, input().split()))
cnt = 0

def sosu(x):
  if x == 1:
    return False
  if x == 2 or x == 3:
    return True
    
  for i in range(2, x//2 + 1):
    if x % i == 0:
      return False
  return True

for i in arr:
  if sosu(i):
    cnt += 1

print(cnt)
