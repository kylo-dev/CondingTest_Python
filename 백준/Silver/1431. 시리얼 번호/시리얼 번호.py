n = int(input())

serials = [input() for _ in range(n)]

def sum_num(x):
  result = 0
  for i in x:
    if i.isdigit():
      result += int(i)
  return result

serials.sort(key = lambda x: (len(x), sum_num(x), x))

print("\n".join(serials))