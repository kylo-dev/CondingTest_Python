import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, []] for _ in range(N+1)]

# [1로 만드는 횟수, 사용한 숫자]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, N+1):
  dp[i][0] = dp[i-1][0] + 1
  dp[i][1] = dp[i-1][1] + [i]

  if i % 3 == 0 and dp[i//3][0] < dp[i][0]:
    dp[i][0] = dp[i//3][0] + 1
    dp[i][1] = dp[i//3][1] + [i]
  if i % 2 == 0 and dp[i//2][0] < dp[i][0]:
    dp[i][0] = dp[i//2][0] + 1
    dp[i][1] = dp[i//2][1] + [i]
  
print(dp[N][0])
print(' '.join(map(str, reversed(dp[N][1]))))