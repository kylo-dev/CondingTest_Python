import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(n):
  url, pwd = input().split()
  dict[url] = pwd

for j in range(m):
  ans = input().rstrip()
  print(dict[ans])