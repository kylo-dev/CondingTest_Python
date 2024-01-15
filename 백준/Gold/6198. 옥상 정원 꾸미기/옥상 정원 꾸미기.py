import sys
input = sys.stdin.readline

n = int(input())
building = [int(input()) for _ in range(n)]

stk = []
cnt = 0

for i in range(n):
  while stk and stk[-1] <= building[i]:
    stk.pop()

  stk.append(building[i])
  cnt += len(stk) -1
  
print(cnt)