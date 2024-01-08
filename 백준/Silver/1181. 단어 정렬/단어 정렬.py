import sys
input = sys.stdin.readline

n = int(input())

arr = {}

for i in range(n):
  alp = input().rstrip()
  if alp not in arr:
    arr[alp] = len(alp)

ans = sorted(arr.items(), key = lambda x: (x[1], x[0]))

for i in ans:
  print(i[0])
