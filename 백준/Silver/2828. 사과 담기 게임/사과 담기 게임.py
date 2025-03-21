N, M = map(int, input().split())
J = int(input())

apples = [int(input()) for _ in range(J)]

cnt = 0
now = 1
for apple in apples:
  if now <= apple and now + (M - 1) >= apple:
    continue
  elif now > apple:
    cnt += abs(now - apple)
    now = apple
  else:
    cnt += apple - (now + M - 1)
    now = apple - (M - 1)

print(cnt)