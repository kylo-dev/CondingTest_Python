moum = ['a', 'e', 'i', 'o', 'u']
accept = ['ee', 'oo']

while True:
  x = y = 0
  word = input()

  if word == 'end':
    break

  cnt = 0
  # 모음 개수 카운트
  for i in moum:
    if i in word:
      cnt += 1
  
  if cnt < 1:
    print(f'<{word}> is not acceptable.')
    continue

  # 모음 3개 or 자음 3개 카운트
  for i in range(len(word) - 2):
    if word[i] in moum and word[i+1] in moum and word[i+2] in moum:
      x = 1
    elif not(word[i] in moum) and not(word[i+1] in moum) and not(word[i+2] in moum):
      x = 1
  
  if x == 1:
    print(f'<{word}> is not acceptable.')
    continue
  
  # 같은 글 카운트
  for i in range(len(word) - 1):
    if word[i] == word[i+1]:
      if word[i] == 'e' or word[i] == 'o':
        continue
      else:
        y = 1
  
  if y == 1:
    print(f'<{word}> is not acceptable.')
    continue

  print(f'<{word}> is acceptable.')