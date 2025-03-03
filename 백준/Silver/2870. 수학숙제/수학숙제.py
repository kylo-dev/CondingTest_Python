
M = int(input())

result = []
for i in range(M):
  res = ''

  word = input()
  for w in word:
    if w.isnumeric():
      res += w
    else:
      if len(res):
        result.append(res)
      res = ''
  if len(res):
    result.append(res)

for i in range(len(result)):
  result[i] = int(result[i])

result.sort()
for i in result:
  print(i)