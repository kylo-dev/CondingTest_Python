import sys
input = sys.stdin.readline

n = int(input())

stk = []
op = []
count = 1
temp = True

for i in range(n):
  num = int(input())
  while count <= num:
    stk.append(count)
    op.append("+")
    count += 1

  if stk[-1] == num:
    stk.pop()
    op.append("-")
  else:
    temp = False

if temp == False:
  print("NO")
else:
  for i in op:
    print(i)