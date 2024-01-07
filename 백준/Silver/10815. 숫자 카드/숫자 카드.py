import sys
input = sys.stdin.readline

n = int(input())
n_cards = list(map(int, input().split()))

n_cards.sort()

m = int(input())
m_cards = list(map(int, input().split()))

def binary(arr, target, start , end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return 0

for i in m_cards:
  print(binary(n_cards,i,0,n-1), end=" ")