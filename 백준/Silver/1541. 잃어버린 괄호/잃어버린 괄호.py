import sys
input = sys.stdin.readline

arr = input().split('-')

tmp = []
for i in arr:
  a = i.split('+')
  sum = 0
  for j in a:
    sum += int(j)
  tmp.append(sum)

n = tmp[0]
for i in range(1, len(tmp)):
  n -= tmp[i]

print(n)