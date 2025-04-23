import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

add_sums = set()
for i in arr:
    for j in arr:
        add_sums.add(i + j)

def check():
    for i in range(N-1, -1, -1):
        for j in range(i + 1):
            if arr[i] - arr[j] in add_sums:
                return arr[i]

print(check())