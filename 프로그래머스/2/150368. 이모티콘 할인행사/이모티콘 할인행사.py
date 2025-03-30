from collections import defaultdict

def solution(users, emoticons):
    
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []
    
    # 1. 서비스 가입자 늘리기
    # 2. 판매액 늘리기
    
    # 이모티콘 할인율 구하기
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
    dfs([0] * len(emoticons), 0)
    
    for d in range(len(discount)):
        plus_user, profit = 0, 0
        
        for user in users:
            emoticon_buy = 0
            for i in range(len(emoticons)):
                if discount[d][i] >= user[0]:
                    emoticon_buy += emoticons[i] * ((100 - discount[d][i]) / 100)
            
            if emoticon_buy >= user[1]:
                plus_user += 1
            else:
                profit += emoticon_buy
        
        if answer[0] < plus_user:
            answer = [plus_user, profit]
        elif answer[0] == plus_user:
            if answer[1] < profit:
                answer = [answer[0], profit]
    return answer