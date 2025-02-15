import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

ans = []
def back(start):
  if len(ans) == M:
    print(' '.join(map(str, ans)))
    return
  
  for i in range(len(arr)):
    if arr[i] in ans:
      continue
    ans.append(arr[i])
    back(start + 1)
    ans.pop()

back(0)