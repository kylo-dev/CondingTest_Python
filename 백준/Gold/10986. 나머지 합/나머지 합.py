import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 정답 개수
answer = 0

total = 0
dp = [0] * M

for i in range(N):
    total += arr[i]
    dp[total % M] += 1

answer = dp[0]

for i in dp:
    answer += i * (i - 1) // 2

print(answer)