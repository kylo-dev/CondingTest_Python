
word = input()

rev_word = reversed(word)
rev = ''.join(rev_word)

if word == rev:
  print(1)
else:
  print(0)