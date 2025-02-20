array = [0 for _ in range(26)]

n = input()
for i in n:
    cnt = ord(i) - 97
    array[cnt] += 1

for j in array:
    print(j, end=' ')