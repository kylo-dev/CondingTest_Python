n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0

for i in reversed(coins):
  cnt = cnt + (k//i)
  k = k % i

print(cnt)
