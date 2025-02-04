str = input()

if not str or str[0] == "_" or str[0].isupper() or str[-1] == "_" or "__" in str:
  print("Error!")
  exit()

isJava = True if "_" not in str else False

if isJava:
  answer = ''
  for i in range(len(str)):
    if str[i].isupper():
      answer += "_" + str[i].lower()
    elif str[i].islower():
      answer += str[i]
    else:
      print("Error!")
      exit()
  print(answer)
else:
  answer = ''
  underbar = False
  for i in range(len(str)):
    if str[i].isupper():
      print("Error!")
      exit()
    elif str[i].isalpha() and not underbar:
      answer += str[i]
    elif str[i] == '_':
      underbar = True
    elif str[i].isalpha() and underbar:
      answer += str[i].upper()
      underbar = False
    elif str[i] == '_' and underbar:
      print("Error!")
      exit()
    else:
      print("Error!")
      exit()
  print(answer)