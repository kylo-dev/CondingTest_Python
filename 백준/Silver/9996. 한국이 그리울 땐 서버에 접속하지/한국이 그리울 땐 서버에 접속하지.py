n = int(input())
pattern = input()

star = pattern.find("*")
start = pattern[0:star]
end = pattern[star+1:]

for _ in range(n):
  ques = input()
  if len(ques) >= len(start) + len(end) and ques.startswith(start) and ques.endswith(end):
    print("DA")
  else:
    print("NE")