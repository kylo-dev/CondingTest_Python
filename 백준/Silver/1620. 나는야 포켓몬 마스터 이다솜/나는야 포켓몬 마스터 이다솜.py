import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocket1 = {}
pocket2 = {}

for i in range(1, n+1):
  name = input().rstrip()

  pocket1[name] = i
  pocket2[i] = name

for j in range(m):

  key_name = input().rstrip()
  if key_name.isdigit():
    print(pocket2[int(key_name)])
  else:
    print(pocket1[key_name])
