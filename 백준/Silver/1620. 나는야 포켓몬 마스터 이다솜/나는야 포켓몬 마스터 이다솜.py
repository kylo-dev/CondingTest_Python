import sys
input = sys.stdin.readline

n, m = map(int , input().split())
dict1 = {}

for i in range(1, n+1):
  key = input().rstrip()
  dict1[key] = i

dict2 = {v:k for k,v in dict1.items()}

for j in range(m):
  qna = input().rstrip()
  if qna.isdigit():
    print(dict2[int(qna)])
  else:
    print(dict1[qna])