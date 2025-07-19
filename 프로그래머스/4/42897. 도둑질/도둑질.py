def solution(money):
    
    # 첫 번째 집 포함 & 마지막 집 미포함
    first = rob(money[:-1])
    
    # 첫 번째 집 미포함 & 마지막 집 포함
    second = rob(money[1:])
    
    return max(first, second)
    

def rob(money):
    N = len(money)
    dp = [0] * N
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, N):
        dp[i] = max(money[i] + dp[i - 2], dp[i - 1])
    
    return max(dp)
    