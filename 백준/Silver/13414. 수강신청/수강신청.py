import sys
input = sys.stdin.readline

k, l = map(int, input().split())

dict = {}

for i in range(l):
  number = input().rstrip()
  dict[number] = i

answer = sorted(dict.items(), key = lambda x :x[1])

if (k > len(answer)):
  k = len(answer)
  
for i in range(k):
  print(answer[i][0])