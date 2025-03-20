N = int(input())
pattern = input()

arr = [input() for _ in range(N)]

star = pattern.find("*")
prefix = pattern[:star]
surfix = pattern[star+1:]

for i in arr:
  if len(pattern) - 1 <= len(i) and i.startswith(prefix) and i.endswith(surfix):
    print("DA")
  else:
    print("NE")