import sys, heapq
input = sys.stdin.readline

N = int(input())
que = []

for i in range(N):
  if not que:
    for i in list(map(int, input().split())):
      heapq.heappush(que, i)
  else:
    for j in list(map(int, input().split())):
      max_num = max(heapq.heappop(que), j)
      heapq.heappush(que, max_num)

que.sort()
print(que[0])