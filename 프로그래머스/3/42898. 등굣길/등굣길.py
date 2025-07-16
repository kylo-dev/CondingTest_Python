def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    puddles = [(y, x) for x, y in puddles]
    
    # 가로 & 세로 초기화
    x, y = 1, 1
    for _ in range(m - 1):
        y += 1
        if (1, y) not in puddles:
            dp[1][y] = 1
        else:
            break
    
    for _ in range(n - 1):
        x += 1
        if (x, 1) not in puddles:
            dp[x][1] = 1
        else:
            break
    
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if (i, j) not in puddles:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    
    return dp[-1][-1] % 1000000007