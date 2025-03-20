import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]

start, end = 1, max(lans)

while start <= end:
  cnt = 0
  mid = (start + end) // 2

  for lan in lans:
    cnt += lan // mid
  
  if cnt >= N:
    start = mid + 1
  else:
    end = mid - 1
print((start+end)//2)