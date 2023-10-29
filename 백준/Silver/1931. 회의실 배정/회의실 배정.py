import sys
input = sys.stdin.readline
# 회의의 수
n = int(input())

arr = []

for i in range(n):
  s, e = map(int, input().split())
  arr.append([s,e])

arr.sort(key = lambda x :(x[1], x[0]))

cnt = end_time = 0

for s, e in arr:
  if s >= end_time:
    cnt += 1
    end_time = e

print(cnt)