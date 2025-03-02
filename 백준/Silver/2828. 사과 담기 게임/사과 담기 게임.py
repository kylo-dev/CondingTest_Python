import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

result = 0
now = 1

for apple in apples:
  if now <= apple and now + (M-1) >= apple:
    continue
  elif now > apple:
    result += abs(apple - now)
    now = apple
  else:
    result += apple - (M - 1) - now
    now = apple - (M - 1)

print(result)