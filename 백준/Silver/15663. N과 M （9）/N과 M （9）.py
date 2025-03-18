N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

visited = [False] * N
answer = []

def back():
  check = 0
  if len(answer) == M:
    print(*answer)
    return

  for i in range(N):
    if check != arr[i] and not visited[i]:
      answer.append(arr[i])
      visited[i] = True
      check = arr[i]
      back()
      answer.pop()
      visited[i] = False

back()