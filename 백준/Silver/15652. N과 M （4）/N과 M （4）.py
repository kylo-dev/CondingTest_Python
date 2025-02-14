N, M = map(int, input().split())

ans = []

def back():

  for i in range(1, N + 1):
    if len(ans) == M:
      print(' '.join(map(str, ans)))
      return
    
    if not ans:
      ans.append(i)
      back()
      ans.pop()
    elif i >= ans[-1]:
      ans.append(i)
      back()
      ans.pop()

back()