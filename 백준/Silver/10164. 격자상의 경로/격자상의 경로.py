

N, M, K = map(int, input().split())
dp = [[0] * M for _ in range(N)]

if K:
    x = (K - 1) // M
    y = (K - 1) % M

    # x, y = 1, 2
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    for i in range(x, N):
        for j in range(y, M):
            if i == x and j == y:
                continue
            if i == x or j == y:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    print(dp[x][y] * dp[-1][-1])
else:
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[-1][-1])