import sys
input = sys.stdin.readline

n = int(input())

dict = {}

for i in range(n):
  name, log = input().split()

  if log == 'enter':
        dict[name] = log
  else:
    del dict[name]

answer = sorted(dict.keys(), key = lambda x: x, reverse=True)

for i in answer:
  print(i)
