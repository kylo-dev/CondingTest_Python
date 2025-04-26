import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())

arr = [1] * N
for _ in range(B):
    n = int(input())
    arr[n-1] = 0

broken = K - sum(arr[:K])
min_fix = broken

for i in range(K, N):
    if arr[i-K] == 0:
        broken -= 1
    if arr[i] == 0:
        broken += 1
    
    min_fix = min(min_fix, broken)

print(min_fix)