n = int(input())

k = [int(input()) for _ in range(n)]

k.sort()

answers = []

for i in k:
  answers.append(i*n)
  n -= 1

print(max(answers))