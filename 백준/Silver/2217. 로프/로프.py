n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

result = 0

for i in range(n):
  cnt = arr[i] * (len(arr) - i)
  if cnt > result:
    result = cnt
  
print(result)