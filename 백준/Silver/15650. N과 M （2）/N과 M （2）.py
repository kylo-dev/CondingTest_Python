n, m = map(int, input().split())

stk = []

def back():
  if len(stk) == m:
    print(' '.join(map(str, stk)))
    return

  for i in range(1, n + 1):
    if i not in stk:
      if len(stk) == 0:
        stk.append(i)
        back()
        stk.pop()
      elif i > stk[-1]:
        stk.append(i)
        back()
        stk.pop()
  
back()
