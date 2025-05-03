from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    que = deque(zip(progresses, speeds))
    
    while que:
        progress, speed = que.popleft()
        days = math.ceil((100 - progress) / speed)
        cnt = 1
        
        while que and (que[0][0] + que[0][1] * days) >= 100:
            cnt += 1
            que.popleft()
        
        answer.append(cnt)
    
    return answer
    