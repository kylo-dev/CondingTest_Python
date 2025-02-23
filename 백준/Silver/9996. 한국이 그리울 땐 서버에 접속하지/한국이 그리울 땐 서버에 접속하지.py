N = int(input())

pattern = input()
star = pattern.index("*")

start = pattern[:star]
end = pattern[star+1:]

files = [input() for _ in range(N)]

for file in files:
  if len(pattern) - 1 <= len(file) and file.startswith(start) and file.endswith(end):
    print("DA")
  else:
    print("NE")
