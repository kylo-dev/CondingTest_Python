import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

deq = deque(range(1, n+1))

while len(deq) != 1:
  deq.popleft()

  deq.append(deq.popleft())

print(deq[0])