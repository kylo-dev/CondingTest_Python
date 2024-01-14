import sys
input = sys.stdin.readline

n = int(input())

top_list = list(map(int, input().split()))

stk = []
ans = [] # 수신하는 탑의 위치

for i in range(n):
  while stk:
    if stk[-1][1] > top_list[i]:
      ans.append(stk[-1][0] + 1)
      break
    else:
      stk.pop()

  if not stk:
    ans.append(0)
  stk.append([i, top_list[i]])

print(' '.join(map(str, ans)))