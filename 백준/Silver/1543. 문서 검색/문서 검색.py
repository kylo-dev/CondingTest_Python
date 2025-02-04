doc = input()
target = input()

size = len(target)
cnt = 0

while True:
  
  idx = doc.find(target)
  if idx < 0:
    break
  else:
    doc = doc[idx+size:]
    cnt += 1

print(cnt)