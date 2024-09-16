arr = [list(map(int, input().split())) for _ in range(5)]

speak = []
for _ in range(5):
  speak += list(map(int, input().split()))

# 사용자 전체 빙고판 확인하기
def check():
  tmp = 0
  # 가로
  for i in range(5):
    if arr[i] == [0,0,0,0,0]:
      tmp += 1

  # 세로
  for i in range(5):
    if all(arr[j][i] == 0 for j in range(5)):
      tmp += 1

  # 대각선 1
  if (all(arr[i][i] == 0 for i in range(5))):
    tmp += 1

  # 대각선 2
  if (all(arr[i][4-i] == 0 for i in range(5))):
    tmp += 1

  return tmp

cnt = 0
for i in range(25):
  for x in range(5):
    for y in range(5):
      if speak[i] == arr[x][y]:
        arr[x][y] = 0
        cnt += 1
  if cnt >= 12:
    result = check()
    if result >= 3:
      print(cnt)
      break