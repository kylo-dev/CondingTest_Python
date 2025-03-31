import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

instruments = set()

for _ in range(N):
  instrument, able = input().split()
  able = able.replace("Y", "1").replace("N", "0")
  instruments.add(int(able, 2))

instruments -= {0}
if not instruments:
  print(-1)
  exit()

max_cnt = 0
target =  (1 << M) - 1

for i in range(1, N + 1):
  for comb in combinations(instruments, i):
    result = 0
    for c in comb:
      result |= c
    
    sub_ans = target & result
    cnt = bin(sub_ans).count("1")

    if max_cnt < cnt:
      max_cnt = cnt
      answer = i

print(answer)