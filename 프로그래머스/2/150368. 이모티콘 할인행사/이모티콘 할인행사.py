def solution(users, emoticons):
    
    N = len(emoticons)
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []
    
    def dfs(temp, depth):
        if depth == N:
            discount.append(temp[:])
            return
        
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
    
    dfs([0] * N, 0)
    
    for i in range(len(discount)):
        plus_user, profit = 0, 0
        
        for user in users:
            total = 0
            for j in range(N):
                if user[0] <= discount[i][j]:
                    total += emoticons[j] * ((100 - discount[i][j]) / 100)

            if total >= user[1]:
                plus_user += 1
            else:
                profit += total
        
        if answer[0] < plus_user:
            answer = [plus_user, profit]
        elif answer[0] == plus_user and answer[1] < profit:
            answer = [answer[0], profit]
    
    return answer