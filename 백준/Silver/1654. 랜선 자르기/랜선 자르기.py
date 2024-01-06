import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)

while start <= end:
  mid = (start + end) // 2
  lines = 0

  for i in lan:
    lines += i // mid
    
  if lines >= n:
    # 조건 충족 시, 최대의 랜선 길이를 위해 start 값을 키우기
    start = mid + 1
  else:
    # 조건 미충족 시, 조건 만족을 위해 랜선의 길이 줄이기. end 값 줄이기
    end = mid - 1

print(end)