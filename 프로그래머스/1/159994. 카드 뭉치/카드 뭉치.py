def solution(cards1, cards2, goal):
    answer = []
    
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            answer.append(cards1.pop(0))
        elif len(cards2) > 0 and cards2[0] == word:
            answer.append(cards2.pop(0))
        else:
            break
    
    return 'Yes' if answer == goal else 'No'