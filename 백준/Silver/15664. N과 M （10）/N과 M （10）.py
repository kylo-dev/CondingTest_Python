N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))
visited = [False] * N

answer = []

def back():
  if len(answer) == M:
    print(*answer)
    return
  
  check = 0
  for i in range(N):
    if not visited[i] and check != arr[i]:
      if not len(answer):
        visited[i] = True
        check = arr[i]
        answer.append(arr[i])
        back()
        answer.pop()
        visited[i] = False
      elif answer[-1] <= arr[i]:
        visited[i] = True
        check = arr[i]
        answer.append(arr[i])
        back()
        answer.pop()
        visited[i] = False

back()