def solution(friends, gifts):
    
    # 이번 달까지 선물을 더 준 사람이 -> 담달에 선물을 받는다.
    
    # 기록이 없거나, 주고받은 수 같다면 -> 선물 지수가 큰 사람이 받는다.
    # 선물 지수 : 준 선물 - 받은 선물 (No 절댓값)
    
    # gift : "A B" A -> B
    
    # 준 선물 관리
    friend = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for gift in gifts:
        A, B = gift.split()
        a_idx = friends.index(A)
        b_idx = friends.index(B)
        friend[a_idx][b_idx] += 1
    
    # 받은 선물 관리
    get_gift = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        total = 0
        for j in range(len(friends)):
            total += friend[j][i]
        get_gift[i] = total
    
    # 선물 지수
    gift_jisu = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        gift_jisu[i] = sum(friend[i]) - get_gift[i]
        
    # 담달 받을 선물 구하기
    answer = [0 for _ in range(len(friends))]
    
    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            if i != j:
                if friend[i][j] > friend[j][i]:
                    count += 1
                elif (friend[i][j] == friend[j][i]) or (friend[i][j] == 0 and friend[j][i] == 0):
                    if gift_jisu[i] > gift_jisu[j]:
                        count += 1
        answer[i] = count
    
    print(answer)
    return max(answer)
        
        