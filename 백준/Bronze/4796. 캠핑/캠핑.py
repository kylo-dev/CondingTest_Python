def camping(idx):
  l, p, v = map(int, input().split())

  if l == 0 and p == 0 and v == 0:
    return False

  sum = 0

  while v > 0:
    if v < l:
      sum += v
    else:
      sum += l
    v -= p
  
  print(f'Case {idx}: {sum}')

idx = 1
while True:
  if (camping(idx) == False):
    break
  else:
    idx += 1