import bisect

T = int(input())


for _ in range(T):
  A, B = map(int, input().split())
  a_list = list(map(int, input().split()))
  b_list = sorted(list(map(int, input().split())))

  cnt = 0

  for a in a_list:
    cnt += bisect.bisect_right(b_list, a - 1)
  
  print(cnt)