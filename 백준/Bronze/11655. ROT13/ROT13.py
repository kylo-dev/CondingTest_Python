
S = input()

res = ''

for i in S:
  if 'a' <= i <= 'z':
    i = ord(i) + 13
    if i > 122:
      i -= 26
    res += chr(i)
  elif 'A' <= i <= 'Z':
    i = ord(i) + 13
    if i > 90:
      i -= 26
    res += chr(i)
  else:
    res += i


print(res)