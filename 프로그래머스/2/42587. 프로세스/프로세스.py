from collections import deque

def solution(priorities, location):
    
    que = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    answer = []
    
    while que:
        
        idx, priority = que.popleft()
        
        if que and priority < max([priority for _, priority in que]):
            que.append((idx, priority))
        else:
            answer.append(idx)
    
    return answer.index(location) + 1
            