import sys
input = sys.stdin.readline
n = int(input())

peo = {}

for i in range(n):
  a, b = input().split()

  if b == 'enter':
    peo[a] = 1
  else:
    del peo[a]

peo = sorted(peo, key = lambda x : x, reverse=True)

for i in peo:
  print(i)