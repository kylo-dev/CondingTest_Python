import sys
input = sys.stdin.readline

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, tol):
  global cnt

  if idx >= n:
      return

  tol += n_list[idx]

  if tol == s:
      cnt += 1
  
  subset_sum(idx+1, tol)
  subset_sum(idx+1, tol - n_list[idx])


subset_sum(0,0)
print(cnt)