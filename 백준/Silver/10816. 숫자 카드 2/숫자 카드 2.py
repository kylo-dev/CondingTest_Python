import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
test = list(map(int, input().split()))

cards = sorted(Counter(cards).items(), key = lambda x : x)
cards = dict(cards)

answer = []

for i in test:
  if i in cards:
    answer.append(cards[i])
  else:
    answer.append(0)

print(' '.join(map(str, answer)))
