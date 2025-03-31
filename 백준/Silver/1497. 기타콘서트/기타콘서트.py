import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

instruments = set()

for _ in range(N):
  instrument, able = input().split()
  able = int(able.replace("Y", "1").replace("N", "0"), 2)
  if able:
    instruments.add(able)

if not instruments:
  print(-1)
  exit()

target =  (1 << M) - 1
max_cnt = 0
answer = N

for i in range(1, N + 1):
  for comb in combinations(instruments, i):
    result = 0
    for c in comb:
      result |= c
    
    cnt = bin(result).count("1")

    if cnt > max_cnt:
      max_cnt = cnt
      answer = i

print(answer)