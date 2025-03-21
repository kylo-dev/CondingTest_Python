N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

cnt = 0
now = 1
for apple in apples:
  if now <= apple <= now + (M - 1):
    continue
  elif now > apple:
    cnt += abs(apple - now)
    now = apple
  else:
    cnt += apple - (now + M - 1)
    now = apple - (M - 1)
print(cnt)