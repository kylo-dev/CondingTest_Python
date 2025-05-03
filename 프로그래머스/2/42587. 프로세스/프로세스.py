from collections import deque

def solution(priorities, location):
    
    answer = []
    que = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    
    while que:
        idx, priority = que.popleft()
        
        if que and priority < max([priority for _, priority in que]):
            que.append((idx, priority))
        else:
            answer.append(idx)
            # cnt += 1
            # if idx == location:
            #     answer = cnt
            #     break
    return answer.index(location) + 1
        