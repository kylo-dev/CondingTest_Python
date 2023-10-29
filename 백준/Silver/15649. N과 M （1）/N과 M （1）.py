n, m = map(int, input().split())

stk = []

def dfs():
  if len(stk) == m:
    print(' '.join(map(str, stk)))
    return

  for i in range(1, n+1):
    if i not in stk:
      stk.append(i)
      dfs()
      stk.pop()

dfs()
