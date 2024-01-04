import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp = sorted(list(set(arr)))

dict = {tmp[i]: i for i in range(len(tmp))}

for i in arr:
  print(dict.get(i), end=" ")