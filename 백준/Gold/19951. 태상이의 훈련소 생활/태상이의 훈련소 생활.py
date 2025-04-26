import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
diff = [0] * (N + 1)

for _ in range(M):
    a, b, amount = map(int, input().split())
    diff[a - 1] += amount
    diff[b] -= amount

for i in range(1, N):
    diff[i] += diff[i - 1]

for i in range(N):
    arr[i] += diff[i]

print(' '.join(map(str, arr)))