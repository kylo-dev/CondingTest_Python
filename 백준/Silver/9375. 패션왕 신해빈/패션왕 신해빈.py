import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  dict = {}
  sum = 1
  
  m = int(input())
  for j in range(m):
    a, b = input().split()
    if b in dict:
      dict[b] += 1
    else:
      dict[b] = 1

  for k in dict.keys():
    sum *= (dict[k]+1)

  print(sum - 1)
