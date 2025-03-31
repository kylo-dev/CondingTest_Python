def solution(users, emoticons):
    
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discounts = []
    N = len(emoticons)
    
    # 할인 경우의 수 
    def dfs(temp, depth):
        if depth == N:
            discounts.append(temp[:])
            return
        
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
        
    dfs([0] * N, 0)
    
    for i in range(len(discounts)):
        plus_user, profit = 0, 0
        for user in users:
            total = 0
            for j in range(N):
                if user[0] <= discounts[i][j]:
                    total += emoticons[j] * ((100 - discounts[i][j]) / 100)
            
            if total >= user[1]:
                plus_user += 1
            else:
                profit += total
        
        if answer[0] < plus_user:
            answer = [plus_user, profit]
        elif answer[0] == plus_user and answer[1] < profit:
            answer = [plus_user, profit]
    
    return answer
            